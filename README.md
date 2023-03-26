"# GoogleDriveAPIDownloader" 
Summary: The Python script uses the Google Drive API to list the account information and then lists the files that 
can be downloaded. The user can then select a file to download and the Python script will download the selected 
file. The script utilizes the OAuth 2.0 protocol for authentication, and the Google Drive API for file management. 
The user interacts with the script through a command-line interface, providing authentication credentials and 
selecting a file to download. Once the file is downloaded, it is saved to a local directory specified by the user. 
The Python script provides a simple and efficient way for users to interact with their Google Drive account 
and download files from it.


#Steps to create a credentials.json file

1. Go to the Google Cloud Console (https://console.cloud.google.com/) and sign in with your Google account.

2. Click on the project selector dropdown at the top of the page and create a new project by clicking on the 
"New Project" button.

3. Give your project a name, select a billing account (if necessary), and click "Create".

4. Once your project is created, select it from the project selector dropdown at the top of the page.

5. Go to the "APIs & Services" dashboard and click on the "Credentials" tab.

6. Click the "Create Credentials" button and select "OAuth client ID" from the dropdown.

7. Select "Desktop app" as the application type and give your client ID a name.

8. Click "Create" and you should be presented with a dialog box containing your client ID and client secret.

9. Download the client secret file and keep it in a safe place.

10. Rename it to credentials.json



# steps to use googleDriveAPI.py
1. Run the py file

2. follow instructions on the console


References
https://developers.google.com/drive/api
https://learndataanalysis.org/google-drive-api-in-python-getting-started-lesson-1/
