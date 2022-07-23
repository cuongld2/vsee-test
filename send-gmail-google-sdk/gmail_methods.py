from __future__ import print_function

import base64
from email.message import EmailMessage

import google.auth
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError


def gmail_send_email(creds):
    """Create and insert a draft email.
       Print the returned draft's message and id.
       Returns: Draft object, including draft id and message meta data.

      Load pre-authorized user credentials from the environment.
      TODO(developer) - See https://developers.google.com/identity
      for guides on implementing OAuth2 for the application.
    """

    try:
        service = build('gmail', 'v1', credentials=creds)
        message = EmailMessage()

        message.set_content('This is automated draft mail')

        message['To'] = 'ledinhcuong23072020@gmail.com'
        message['From'] = 'ledinhcuong99@gmail.com'
        message['Subject'] = 'Automated draft'

        # encoded message
        encoded_message = base64.urlsafe_b64encode(message.as_bytes()) \
            .decode()

        create_message = {
            'raw': encoded_message
        }
        # pylint: disable=E1101
        send_message = (service.users().messages().send
                        (userId="me", body=create_message).execute())
        print(F'Message Id: {send_message["id"]}')
    except HttpError as error:
        print(F'An error occurred: {error}')
        send_message = None
    return send_message["id"]

def get_message_sent(creds):
    try:
        # Call the Gmail API
        service = build('gmail', 'v1', credentials=creds)
        response = service.users().messages().list(userId='me',q='to:ledinhcuong23072020@gmail.com').execute()
        messages = []
        if 'messages' in response:
            messages.extend(response['messages'])
            print(f'{messages}')
    
    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f'An error occurred: {error}') 
    assert len(messages) == 1
    return messages

def delete_message_sent(creds, message_id):
    try:
        # Call the Gmail API
        service = build('gmail', 'v1', credentials=creds)
        response = service.users().messages().delete(userId='me',id=message_id).execute()
    
    except HttpError as error:
        # TODO(developer) - Handle errors from gmail API.
        print(f'An error occurred: {error}') 
    return response
