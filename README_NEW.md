# Radha API - YouTube Audio Backend

A FastAPI backend that provides YouTube audio URLs for music bots and applications, available at [www.radhaapi.me](https://www.radhaapi.me).

## Features

✅ **YouTube Audio Extraction**: Get direct audio URLs from YouTube videos  
✅ **API Key Authentication**: Secure access with Bearer token authentication  
✅ **Search Integration**: Search YouTube and get the best audio result  
✅ **Error Handling**: Comprehensive error handling for all edge cases  
✅ **Frontend Dashboard**: Web interface to generate API keys and test endpoints  
✅ **CORS Support**: Ready for frontend integration  
✅ **Custom Domain**: Available at www.radhaapi.me

## Live API

The API is deployed and accessible at:
- **Production URL**: [https://www.radhaapi.me](https://www.radhaapi.me)
- **Status Page**: [https://www.radhaapi.me/status](https://www.radhaapi.me/status)

## Quick Start

### Windows
```bash
# Double-click start_server.bat or run:
start_server.bat
```

### Manual Setup
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Start server
python main.py
```

## API Endpoints

### 🔐 Authentication
All protected endpoints require an API key in the Authorization header:
```
Authorization: Bearer YOUR_API_KEY
```

### 📡 Endpoints

#### `POST /generate-api-key`
Generate a new API key (no authentication required)

**Response:**
```json
{
    "api_key": "generated_key_here",
    "message": "New API key generated successfully"
}
```

#### `GET /get-audio?query=<search_term>`
Get YouTube audio URL for a search query

**Headers:**
```
Authorization: Bearer YOUR_API_KEY
```

**Parameters:**
- `query` (required): YouTube search query

**Response:**
```json
{
    "title": "Song Title",
    "duration": 230,
    "audio_url": "https://direct-audio-url",
    "thumbnail": "https://thumbnail-url",
    "video_id": "youtube_video_id"
}
```

**Error Responses:**
- `400`: Invalid query
- `403`: Missing or invalid API key
- `404`: No videos found
- `500`: YouTube extraction failed

## Usage Examples

### cURL
```bash
# Generate API key
curl -X POST "https://www.radhaapi.me/generate-api-key"

# Get audio URL
curl -X GET "https://www.radhaapi.me/get-audio?query=imagine+dragons+believer" \
     -H "Authorization: Bearer YOUR_API_KEY"
```

### Python (for Pyrogram bot)
```python
import requests

API_BASE = "https://www.radhaapi.me"
API_KEY = "your_api_key_here"

def get_youtube_audio(query):
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.get(f"{API_BASE}/get-audio", 
                          params={"query": query}, 
                          headers=headers)
    
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"API Error: {response.json()}")

# Usage
audio_data = get_youtube_audio("your favorite song")
print(f"Audio URL: {audio_data['audio_url']}")
```

## Deployment

See the [RADHAAPI_ME_SETUP.md](RADHAAPI_ME_SETUP.md) file for detailed deployment instructions to Render.com with the custom domain.

## Frontend Dashboard

The web dashboard is available at [www.radhaapi.me](https://www.radhaapi.me) where you can:
- Generate new API keys
- Test the audio API
- View API documentation

## Security Notes

- API keys are stored in memory (for production, use a database)
- The default API key is printed when the server starts
- CORS is currently set to allow all origins (configure for production)

## Dependencies

- **FastAPI**: Web framework
- **yt-dlp**: YouTube downloader and metadata extractor
- **uvicorn**: ASGI server

## Error Handling

The API includes comprehensive error handling for:
- Invalid API keys
- Missing parameters
- YouTube extraction failures
- Network issues
- Invalid video URLs

## For Production

For production deployment:
1. Use a proper database for API key storage
2. Configure CORS for your specific domains
3. Add rate limiting
4. Use HTTPS
5. Set up proper logging

## Support

The API is designed to work with:
- Pyrogram music bots
- Telegram voice chat applications
- Any application needing YouTube audio URLs
