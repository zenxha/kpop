
import requests
import json
# http://ws.audioscrobbler.com/2.0/?method=track.getsimilar&artist=official+hige+dandism&track=pretender&api_key=630846faaf3ca8d5cf4d712e56bd4989&format=json
class Song:
    """Initializer of class takes series parameter and returns Class Object"""
    def __init__(self, artist, song):
        self._artist = artist
        self._song = song
    def get_similar(self):
        artist_query_name = self._artist.replace(' ', '+')
        song_query_name = self._song.replace(' ', '+')
        response = requests.get('http://ws.audioscrobbler.com/2.0/?method=track.getsimilar&artist='+artist_query_name+'&track='+song_query_name+'&api_key=630846faaf3ca8d5cf4d712e56bd4989&format=json')

        return response.json()

