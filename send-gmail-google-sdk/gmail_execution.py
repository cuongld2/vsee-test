from __future__ import print_function
from operator import ge

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from gmail_methods import gmail_send_email,get_message_sent,delete_message_sent
from gmail_credentials import get_gmail_credentials

def main():
    creds=get_gmail_credentials()
    message_id = gmail_send_email(creds)
    get_message_sent(creds)
    delete_message_sent(creds,message_id)
        
if __name__ == '__main__':
    main()