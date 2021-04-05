import requests
import json
import os

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

# http://ws.audioscrobbler.com/2.0/?method=track.getsimilar&artist=official+hige+dandism&track=pretender&api_key=630846faaf3ca8d5cf4d712e56bd4989&format=json
class Song:
    """Initializer of class takes series parameter and returns Class Objectg"""
    def __init__(self, artist, song):
        self._artist = artist
        self._song = song
    def get_similar(self):
        artist_query_name = self._artist.replace(' ', '+')
        song_query_name = self._song.replace(' ', '+')
        response = requests.get('http://ws.audioscrobbler.com/2.0/?method=track.getsimilar&artist='+artist_query_name+'&track='+song_query_name+'&api_key=630846faaf3ca8d5cf4d712e56bd4989&format=json')

        return response.json()

class Video:
    def __init__(self, creator, vidname):
        self._creator = creator
        self._vidname = vidname
    scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

    def main(self):
        # Disable OAuthlib's HTTPS verification when running locally.
        # *DO NOT* leave this option enabled in production.
        os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        api_service_name = "youtube"
        api_version = "v3"
        client_secrets_file = "YOUR_CLIENT_SECRET_FILE.json"

        # Get credentials and create an API client
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            client_secrets_file, scopes)
        credentials = flow.run_console()
        youtube = googleapiclient.discovery.build(
            api_service_name, api_version, credentials=credentials)

        request = youtube.channels().list(
            part="contentDetails",
            forUsername="AOMGOFFICIAL"
        )
        response = request.execute()

        return(response)
