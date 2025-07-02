# Radha API - Deployment Guide

This guide will help you deploy the Radha API to Render.com.

## Prerequisites

1. Create a [Render.com](https://render.com) account
2. Install Git and have your project in a Git repository

## Deployment Steps

### Option 1: Deploy via Blueprint (Recommended)

1. **Push your code to GitHub**:
   - Create a new GitHub repository
   - Push your code to the repository

2. **Deploy with Blueprint**:
   - Go to the Render Dashboard: https://dashboard.render.com/
   - Click "New" and select "Blueprint"
   - Connect your GitHub account if not already connected
   - Select the repository containing your Radha API project
   - Click "Apply Blueprint"
   - Render will automatically deploy the service based on the `render.yaml` file

### Option 2: Manual Deployment

1. **Login to Render**:
   - Go to https://dashboard.render.com/ and sign in

2. **Create a Web Service**:
   - Click "New" and select "Web Service"
   - Connect your repository
   - Choose the repository with your Radha API project

3. **Configure the Service**:
   - Name: `radha-api` (or your preferred name)
   - Environment: `Python`
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - Select the appropriate region and instance type

4. **Set Environment Variables**:
   - No specific environment variables needed for this project

5. **Deploy**:
   - Click "Create Web Service"

## After Deployment

- Your API will be available at `https://radha-api.onrender.com` (or the URL Render assigns)
- The dashboard will be accessible at the root URL
- Use the auto-generated API key shown in the dashboard or generate a new one

## Testing the Deployment

1. Visit the deployed URL in your browser
2. Generate an API key using the dashboard
3. Test the `/get-audio` endpoint with a search query

## Troubleshooting

If your deployment encounters issues:

1. Check the Render logs for error messages
2. Ensure all dependencies are listed in `requirements.txt`
3. Verify the start command is correct
4. Test locally before deploying again

For any issues, refer to [Render's documentation](https://render.com/docs) or contact their support.
