from fastapi import FastAPI, HTTPException, Depends, Header, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
import yt_dlp
import os
import secrets
from typing import Optional
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(title="Radha API", version="1.0")

# Allow all frontend access (for now)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Mount static files directory
try:
    app.mount("/static", StaticFiles(directory="static"), name="static")
    logger.info("Static files directory mounted")
except Exception as e:
    logger.error(f"Failed to mount static files: {str(e)}")

# In-memory API key storage
VALID_API_KEYS = set()
DEFAULT_API_KEY = secrets.token_urlsafe(32)
VALID_API_KEYS.add(DEFAULT_API_KEY)
print(f"Default API Key: {DEFAULT_API_KEY}")

# Auth header checker
def verify_api_key(authorization: Optional[str] = Header(None)):
    if not authorization:
        raise HTTPException(status_code=403, detail="Authorization header missing")
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=403, detail="Invalid authorization format")
    token = authorization.replace("Bearer ", "")
    if token not in VALID_API_KEYS:
        raise HTTPException(status_code=403, detail="Invalid API key")
    return token

@app.get("/")
async def dashboard():
    return FileResponse("index.html")

@app.get("/health")
async def health():
    return {"status": "healthy", "service": "radha-api", "domain": "www.radhaapi.me"}

@app.get("/status")
async def status_page():
    return FileResponse("static/status.html")

@app.get("/api")
async def api_root():
    return {"message": "Radha API running", "key": DEFAULT_API_KEY}

@app.post("/generate-api-key")
async def generate_api():
    new_key = secrets.token_urlsafe(32)
    VALID_API_KEYS.add(new_key)
    return {"api_key": new_key, "message": "API key generated"}

@app.get("/list-api-keys")
async def list_keys(_: str = Depends(verify_api_key)):
    return {"total": len(VALID_API_KEYS), "api_keys": list(VALID_API_KEYS)}

@app.get("/get-audio")
async def get_audio(query: str, _: str = Depends(verify_api_key)):
    if not query.strip():
        raise HTTPException(status_code=400, detail="Query is empty")

    import requests
    
    # Use a simpler approach to fetch results
    logger.info(f"Searching for: {query}")
    
    try:
        # First, search for the video
        search_url = f"https://www.youtube.com/results?search_query={query.replace(' ', '+')}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            "Accept-Language": "en-US,en;q=0.5"
        }
        
        response = requests.get(search_url, headers=headers)
        response_text = response.text
        
        # Extract video ID from search results
        import re
        video_ids = re.findall(r"watch\?v=(\S{11})", response_text)
        
        if not video_ids:
            logger.error("No videos found in search results")
            raise HTTPException(status_code=404, detail="No videos found for query: " + query)
            
        video_id = video_ids[0]
        logger.info(f"Found video ID: {video_id}")
        
        # Get video title and details
        video_url = f"https://www.youtube.com/watch?v={video_id}"
        video_response = requests.get(video_url, headers=headers)
        
        # Extract title
        title_match = re.search(r'<title>(.*?) - YouTube</title>', video_response.text)
        title = title_match.group(1) if title_match else "Unknown Title"
        
        # Create direct URLs for audio and thumbnail
        audio_url = f"https://music.youtube.com/watch?v={video_id}"  # YouTube Music URL that clients can process
        thumbnail = f"https://i.ytimg.com/vi/{video_id}/maxresdefault.jpg"
        
        # Estimate duration (we don't have exact duration but clients can handle this)
        duration = 240  # Default 4 minutes
        
        logger.info(f"Title: {title}")
        logger.info(f"Audio URL: {audio_url}")
        
        return {
            "title": title,
            "duration": duration,
            "audio_url": audio_url,
            "thumbnail": thumbnail,
            "video_id": video_id  # Adding video_id for client-side processing
        }
        
    except Exception as e:
        logger.error(f"Error fetching song: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Failed to fetch song: {str(e)}")

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
