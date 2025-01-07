from appwrite.client import Client
from appwrite.services.databases import Databases
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os
import secrets

def main(req, res):
    try:
        # Initialize Appwrite
        client = Client()
        client.set_endpoint(os.environ.get('APPWRITE_ENDPOINT'))
        client.set_project(os.environ.get('APPWRITE_PROJECT_ID'))
        client.set_key(os.environ.get('APPWRITE_API_KEY'))
        
        database = Databases(client)

        # Extract document from event payload
        document = req.body.get('events', [{}])[0].get('data', {})
        name = document.get('name')
        email = document.get('email')

        if not name or not email:
            return res.json({
                'success': False,
                'message': 'Missing name or email in document.'
            })

        # Generate secure token
        token = secrets.token_hex(32)

        # Update document with token
        database_id = os.environ.get('APPWRITE_DATABASE_ID')
        collection_id = os.environ.get('APPWRITE_COLLECTION_ID')
        
        database.update_document(
            database_id=database_id,
            collection_id=collection_id,
            document_id=document['$id'],
            data={'token': token}
        )

        # Generate tokenized URL
        tokenized_url = f"{os.environ.get('FRONTEND_URL')}/access?token={token}"

        # Create email message
        message = Mail(
            from_email=os.environ.get('SENDGRID_SENDER_EMAIL'),
            to_emails=email,
            subject='Access Your Web App Service',
            html_content=f'''
                <p>Hello {name},</p>
                <p>Welcome! You've been granted access to our web app service. To start using the service, please click the link below:</p>
                <a href="{tokenized_url}" target="_blank">Access Your Web App</a>
                <p>This link is unique to you, so please keep it secure. If you did not sign up for this service, please disregard this email.</p>
                <br>
                <p>Thank you,<br>The Team</p>
            '''
        )

        # Send email using SendGrid
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        sg.send(message)

        return res.json({
            'success': True,
            'message': 'Token generated and email sent.'
        })

    except Exception as error:
        print(f"Error: {str(error)}")
        return res.json({
            'success': False,
            'message': 'An error occurred.',
            'error': str(error)
        })
