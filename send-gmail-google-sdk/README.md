### 1. Install
sudo apt install python3-testresources

### 2. Put credentials.json file into project
credentials.json file is retrieved from google console by creating new project, and get client_id json option in API credentials
token.json file will be automatically created the first time you run the script

### 3. Run the script

# There are 4 steps in the script:
- Retrieve gmail credentials by calling get_gmail_credentials method
- Send the email to recepient by calling gmail_send_email
- Check the email is sent by using get_message_sent with the help of gmail query message (query for recipient email), assert it must be equal 1
- Remove the email that is just sent by using delete_message_sent

# Run the script

venv/bin/python3.8 gmail_execution.py