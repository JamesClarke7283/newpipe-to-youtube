# Introduction

# Get the subscriptions from newpipe
1. Navigate to your Subscriptions
2. Click the virtical 3 dot button. 
3. Click Export to
4. Save your subscriptions file

# Get the Credentials File

Google Developer Console: Navigate to the Google Developer Console.

Create Project: If you don't already have a project, create a new one by clicking the "Select a project" dropdown at the top-right, then click on "New Project", and follow the prompts.

Enable API: Once you're in the project dashboard, click on "Dashboard" in the left sidebar, then click on "+ ENABLE APIS AND SERVICES". Search for "YouTube Data API v3" and enable it.

Create Credentials: After enabling the API, you'll be taken to the API page. Click on "Create credentials" at the top. Here, you'll be asked a series of questions:

Which API are you using?: YouTube Data API v3
Where will you be calling the API from?: Desktop app
What data will you be accessing?: User data
Click "What credentials do I need?" after answering these.

OAuth 2.0 Client ID: Create an OAuth 2.0 client ID. You can name it whatever you want. You'll be prompted to configure the OAuth consent screen. For the purposes of a personal project, you can use the "External" user type. Fill in the necessary details. You can skip optional fields.

Download Credentials: Once the OAuth client ID is created, you'll see a download button (it looks like a down arrow). Click that to download your credentials.json file.

Place in Directory: Place this downloaded credentials.json in the same directory as your Python script.

That's it! Now you should be able to run the Python script to authenticate against the YouTube Data API v3 using these credentials. Let me know if you have more questions!

# Usage
```bash
git clone [URL]
cd newpipe-to-youtube
python3 -m venv .venv
python3 -m pip install -r requirements.txt
python3 main.py /path/to/subscriptions/file.json
```

And you should see a popup in your browser asking to sign into your user. Sign into the account you want your subscriptions imported to. And you should be good to go!