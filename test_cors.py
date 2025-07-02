import requests
import json

# Use your actual Railway URL here
BASE_URL = "https://www.radhaapi.me"

def test_generate_api_key():
    print(f"Testing API key generation at {BASE_URL}/generate-api-key")
    
    # Test OPTIONS request (preflight)
    print("\n1. Testing OPTIONS preflight request...")
    options_response = requests.options(
        f"{BASE_URL}/generate-api-key", 
        headers={
            'Origin': 'https://www.radhaapi.me',
            'Access-Control-Request-Method': 'POST',
            'Access-Control-Request-Headers': 'Content-Type'
        }
    )
    print(f"OPTIONS Status: {options_response.status_code}")
    print(f"OPTIONS Headers: {dict(options_response.headers)}")
    
    # Test POST request
    print("\n2. Testing POST request...")
    post_response = requests.post(
        f"{BASE_URL}/generate-api-key",
        headers={
            'Content-Type': 'application/json',
            'Origin': 'https://www.radhaapi.me'
        },
        data=json.dumps({})
    )
    print(f"POST Status: {post_response.status_code}")
    print(f"POST Headers: {dict(post_response.headers)}")
    try:
        print(f"POST Response: {post_response.json()}")
    except:
        print(f"POST Response (raw): {post_response.text}")
    
    # Test GET fallback
    print("\n3. Testing GET fallback...")
    get_response = requests.get(f"{BASE_URL}/generate-api-key-temp")
    print(f"GET Status: {get_response.status_code}")
    try:
        print(f"GET Response: {get_response.json()}")
    except:
        print(f"GET Response (raw): {get_response.text}")

if __name__ == "__main__":
    test_generate_api_key()
