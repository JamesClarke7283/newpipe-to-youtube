# NewPipe to YouTube Subscriptions Transfer

## Introduction

This command-line application is designed to transfer your video channel subscriptions from NewPipe to your YouTube account. NewPipe is a libre software YouTube client that you may use on Android. While NewPipe is awesome, sometimes you might want to sync your subscriptions back to your main YouTube account. This Python-based tool makes the process a breeze.

## Get the Subscriptions from NewPipe

1. Open the NewPipe app on your Android device.
2. Navigate to your Subscriptions tab.
3. Click the vertical 3-dot button usually located at the top-right corner.
4. Choose "Export to" from the dropdown.
5. Save your subscriptions file. It will be in JSON format.

## Get the Credentials File

### Google Developer Console

1. Navigate to the [Google Developer Console](https://console.developers.google.com/).
2. **Create Project**: If you don't already have a project, create a new one by clicking the "Select a project" dropdown at the top-right, then click on "New Project", and follow the prompts.
3. **Enable API**: Once you're in the project dashboard, click on "Dashboard" in the left sidebar, then click on "+ ENABLE APIS AND SERVICES". Search for "YouTube Data API v3" and enable it.
4. **Create Credentials**: After enabling the API, you'll be taken to the API page. Click on "Create credentials" at the top.

    - **Which API are you using?**: YouTube Data API v3
    - **Where will you be calling the API from?**: Desktop app
    - **What data will you be accessing?**: User data
    
    Click "What credentials do I need?" after answering these questions.

5. **OAuth 2.0 Client ID**: Create an OAuth 2.0 client ID. You'll be prompted to configure the OAuth consent screen. For the purposes of a personal project, you can use the "External" user type. Fill in the necessary details. You can skip optional fields.
6. **Download Credentials**: Once the OAuth client ID is created, you'll see a download button (it looks like a down arrow). Click that to download your `credentials.json` file.
7. **Place in Directory**: Place this downloaded `credentials.json` in the same directory as your Python script.

## Usage

To use the application, follow these steps:

```bash
git clone [URL]
cd newpipe-to-youtube
python3 -m venv .venv
source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
python3 -m pip install -r requirements.txt
python3 main.py /path/to/subscriptions/file.json
```

After running the last command, a popup should appear in your browser asking you to sign into your Google account. Sign into the account where you want your subscriptions to be imported. Once authenticated, the script will automatically start the subscription process.