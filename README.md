# Access Token Function

This Appwrite function generates secure access tokens and sends them via email using SendGrid.

## Setup Instructions

1. **Create Appwrite Project**
   - Go to your Appwrite Console
   - Create a new project or use an existing one
   - Note down the Project ID

2. **Database Setup**
   - Create a new database
   - Create a collection with the following attributes:
     - `name` (string)
     - `email` (string)
     - `token` (string)
   - Note down the Database ID and Collection ID

3. **SendGrid Setup**
   - Create a SendGrid account if you don't have one
   - Verify your sender email address
   - Create an API key with email sending permissions
   - Note down the API key

4. **Environment Variables**
   Set the following environment variables in your Appwrite Console:
   ```
   APPWRITE_ENDPOINT=https://cloud.appwrite.io/v1
   APPWRITE_PROJECT_ID=your-project-id
   APPWRITE_API_KEY=your-api-key
   APPWRITE_DATABASE_ID=your-database-id
   APPWRITE_COLLECTION_ID=your-collection-id
   SENDGRID_API_KEY=your-sendgrid-api-key
   SENDGRID_SENDER_EMAIL=your-verified-sender@email.com
   FRONTEND_URL=https://your-frontend-url.com
   ```

5. **Deploy Function**
   ```bash
   # Install Appwrite CLI
   npm install -g appwrite-cli

   # Login to Appwrite
   appwrite login

   # Deploy function
   appwrite deploy function
   ```

## Testing

To test the function:
1. Create a new document in your collection with a name and email
2. The function will generate a token and send an email
3. Check the email for the access link
