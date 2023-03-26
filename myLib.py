from __future__ import print_function
import os
import io
import os.path
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from Google import Create_Service
from googleapiclient.http import MediaIoBaseDownload

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']
API_NAME = 'drive'
API_VERSION = '3'
SCOPES = ['https://www.googleapis.com/auth/drive']

#data struct to hold files and their ids
fileToID = {}

def display_and_load_first_ten():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('drive', 'v3', credentials=creds)

        # Call the Drive v3 API
        results = service.files().list(
            pageSize=10, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])

        if not items:
            print('No files found.')
            return
        print('Files:')
        for item in items:
            print(u'{0}'.format(item['name']))
            fileToID[item['name']] = item['id']
    except HttpError as error:
        print(f'An error occurred: {error}')

def display_and_load_all():
    """Shows all files in the user's Drive."""
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('drive', 'v3', credentials=creds)

    # Initialize variables for pagination
    page_token = None
    all_files = []

    # Loop until there are no more pages of results
    while True:
        # Call the Drive v3 API with pageToken set to the next page token, if there is one
        results = service.files().list(pageSize=1000, fields="nextPageToken, files(id, name)").execute(
            pageToken=page_token)
        items = results.get('files', [])

        # Add the files from this page to the all_files list
        all_files.extend(items)

        # Check if there are more pages
        page_token = results.get('nextPageToken', None)
        if not page_token:
            break

    # Print the names and IDs of all files
    if all_files:
        print('Files/Folder:')
        for item in all_files:
            print(u'{0}'.format(item['name']))
            #adding to a dictionary of this
            fileToID[item['name']] = item['id']
    else:
        print('No files found.')
    print("There are ", str(len(all_files)) + " files/folder")


# Define the scopes to request access to the Drive API
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly']

# Path to the client_secret.json file
CLIENT_SECRET_FILE = 'credentials.json'

# Path to the credentials file
CREDENTIALS_FILE = 'token.json'


#get the necessary creds
def get_credentials():
    # Check if the credentials file exists
    if os.path.exists(CREDENTIALS_FILE):
        creds = Credentials.from_authorized_user_file(CREDENTIALS_FILE, SCOPES)
        return creds

    # If the credentials file does not exist, authenticate the user
    flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET_FILE, SCOPES)
    creds = flow.run_local_server(port=0)

    # Save the credentials for the next run
    with open(CREDENTIALS_FILE, 'w') as token:
        token.write(creds.to_json())
    return creds




# Authorize the API and print account information
creds = get_credentials()
def account_info():
    drive_service = build('drive', 'v3', credentials=creds)
    about = drive_service.about().get(fields='user').execute()
    print('Account information:')
    print(f"Name: {about['user']['displayName']}")
    print(f"Email: {about['user']['emailAddress']}")
    if 'quotaBytesTotal' in about['user']:
        print(f"Storage quota: {int(about['user']['quotaBytesTotal'])/(1024*1024*1024):.2f} GB")
    else:
        print("Storage quota information not available.")

service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)


#download file with file if and it's name
def download(file_id, file_name):
    request = service.files().get_media(fileID = file_id)

    fh = io.ButesTO()
    downloader = MediaIoBaseDownload(fd=fh, request=request)

    done = False
    while done:
        status, done = downloader.next_chunk()
        print('Download progress {0}', status.progress()*100)

    fh.seek()

    with open(os.path.join('./Random Files', file_name), 'wb') as f:
        f.write(fh.read())
        f.close()
