# Deployment Instructions for www.Radhaapi.me

Follow these step-by-step instructions to deploy your Radha API to Render.com with your custom domain www.Radhaapi.me:

## 1. Prepare Your Repository

1. Push your code to a GitHub repository
2. Make sure the following files are included:
   - `main.py`
   - `index.html`
   - `requirements.txt`
   - `render.yaml`
   - `wsgi.py`
   - `static/` directory
   - Other project files

## 2. Deploy to Render.com

1. Go to https://dashboard.render.com/ and sign in
2. Click "New" and select "Blueprint"
3. Connect your GitHub repository
4. Click "Apply Blueprint"
5. Render will automatically detect your `render.yaml` file and set up the service

## 3. Connect Your Custom Domain

1. After deployment is complete, go to the service dashboard
2. Navigate to "Settings" > "Custom Domains"
3. Click "Add Custom Domain"
4. Enter `www.radhaapi.me`
5. Follow Render's instructions to verify domain ownership

## 4. Configure DNS Settings

1. Log in to your domain registrar (where you purchased radhaapi.me)
2. Go to DNS settings for your domain
3. Add a CNAME record:
   - Name/Host: `www`
   - Value/Target: Your Render URL (e.g., `radha-api.onrender.com`)
   - TTL: 3600 or automatic

## 5. SSL Certificate

Render will automatically provision an SSL certificate for your domain once DNS verification is complete. This may take some time.

## 6. Verify Deployment

1. After DNS propagation (may take 24-48 hours), visit https://www.radhaapi.me
2. Check that:
   - The dashboard loads properly
   - You can generate API keys
   - You can test searching for songs
   - The API endpoints return correct data

## 7. Common Issues and Solutions

- **DNS Not Resolving**: Wait for propagation or check DNS settings
- **SSL Certificate Not Working**: Ensure DNS is properly configured
- **API Returning Errors**: Check Render logs for details
- **Songs Not Found**: Verify the YouTube search functionality

## 8. Monitoring

- Monitor your API usage through the Render dashboard
- Check logs for any errors or issues
- Consider setting up alerts for downtime

Your Radha API should now be successfully deployed at www.radhaapi.me!
