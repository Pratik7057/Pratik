# Radha API - Deployment to www.radhaapi.me

This guide will help you deploy the Radha API to Render.com with your custom domain www.radhaapi.me.

## Render.com Deployment

### Step 1: Deploy to Render

1. **Create a Render.com account** if you don't have one already
2. **Push your code to a GitHub repository**
3. **Deploy with Blueprint**:
   - Go to the Render Dashboard: https://dashboard.render.com/
   - Click "New" and select "Blueprint"
   - Connect your GitHub account and select your repository
   - Click "Apply Blueprint"
   - Render will deploy based on your `render.yaml` configuration

### Step 2: Configure Custom Domain

1. **After deployment completes**:
   - Go to your service dashboard on Render
   - Click on "Settings" > "Custom Domains"
   - Click "Add Custom Domain"
   - Enter `www.radhaapi.me`
   - Follow the verification steps

2. **Set up DNS records** for your domain at your domain registrar:
   - Add a `CNAME` record:
     - Name: `www`
     - Value: The Render URL for your service (e.g., `radha-api.onrender.com`)
     - TTL: 3600 (or as recommended)

3. **Wait for DNS propagation**:
   - It can take up to 24-48 hours for DNS changes to propagate
   - Render will show a status indicator for domain verification

## SSL Configuration

Render provides free SSL certificates for your custom domain automatically:

1. **Verify domain ownership**:
   - Follow Render's instructions to verify domain ownership
   - This might require adding a TXT record to your DNS settings

2. **SSL activation**:
   - Once your domain is verified, Render will automatically provision an SSL certificate
   - Your site will be accessible via `https://www.radhaapi.me`

## Testing the Deployment

1. After DNS propagation is complete, visit `https://www.radhaapi.me` in your browser
2. You should see the Radha API dashboard
3. Test the API endpoints to ensure everything is working correctly
4. The API should be accessible at the following URLs:
   - Dashboard: `https://www.radhaapi.me/`
   - Health Check: `https://www.radhaapi.me/health`
   - API Root: `https://www.radhaapi.me/api`
   - Get Audio: `https://www.radhaapi.me/get-audio?query=your_search_query`

## Troubleshooting

- **If your domain doesn't connect**: Verify DNS settings and check propagation using a tool like `https://dnschecker.org`
- **If SSL isn't working**: Ensure domain verification is complete and wait for certificate issuance
- **If API endpoints return errors**: Check Render logs for any issues

## Maintenance

- Your Radha API will remain online as long as your Render account is active
- Free Render instances may spin down after periods of inactivity
- Consider upgrading to a paid plan for production use with high traffic
