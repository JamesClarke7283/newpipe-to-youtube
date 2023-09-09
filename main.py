import json
import argparse
import google.auth
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# YouTube API setup
SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]
API_SERVICE_NAME = "youtube"
API_VERSION = "v3"

# Authenticate YouTube API
def authenticate_youtube():
    creds = None
    if creds and not creds.valid:
        if creds.expired and creds.refresh_token:
            creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
        creds = flow.run_local_server(port=0)

    with open("token.json", "w") as token:
        token.write(creds.to_json())

    return build(API_SERVICE_NAME, API_VERSION, credentials=creds)

# Subscribe to a channel
def subscribe_channel(youtube, channel_id):
    try:
        youtube.subscriptions().insert(
            part="snippet",
            body={
                "snippet": {
                    "resourceId": {
                        "kind": "youtube#channel",
                        "channelId": channel_id
                    }
                }
            }
        ).execute()
    except HttpError as e:
        print(f"An HTTP error {e.resp.status} occurred: {e.content}")

# Main function
def main(args):
    # Load NewPipe subscriptions JSON
    with open(args.newpipe_file, 'r') as f:
        newpipe_data = json.load(f)
    
    # Authenticate YouTube API
    youtube = authenticate_youtube()

    # Subscribe to channels
    for channel in newpipe_data["subscriptions"]:
        print(f"Subscribing to {channel['name']}")
        url = channel['url']
        channel_id = url.split("/")[-1]
        subscribe_channel(youtube, channel_id)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Transfer NewPipe subscriptions to YouTube.")
    parser.add_argument("newpipe_file", help="NewPipe subscriptions JSON file")
    args = parser.parse_args()
    main(args)
