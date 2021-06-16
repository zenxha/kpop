import requests
import json
import os



# http://ws.audioscrobbler.com/2.0/?method=track.getsimilar&artist=official+hige+dandism&track=pretender&api_key=630846faaf3ca8d5cf4d712e56bd4989&format=json
class Song:
    """Initializer of class takes song info parameters and returns Class Object"""

    def __init__(self, artist, song, sorttype):
        self._artist = artist
        self._song = song
        self._sorttype = sorttype

    @property
    def similar_songs_list(self):
        artist_query_name = self._artist.replace(' ', '+')
        song_query_name = self._song.replace(' ', '+')
        response = requests.get('http://ws.audioscrobbler.com/2.0/?method=track.getsimilar&artist=' + artist_query_name + '&track=' + song_query_name + '&api_key=630846faaf3ca8d5cf4d712e56bd4989&format=json')
        res = response.json()

        res_array = []

        if 'similartracks' in res:
            for song in res['similartracks']['track']:
                res_array.append(song)


            if (self._sorttype == 'playcount'):
                res_array.sort(key=lambda x: x['playcount'], reverse=True)
            if (self._sorttype == 'alphabetical'):
                res_array.sort(key=lambda x: x['name'])
            if self._sorttype == 'similarity':
                res_array = res_array
                print(self._sorttype)

            return res_array
        else:
            return [                {
                "name": "Check your parameters again",
                "playcount": 0,
                "match": 0,
                "url": "https://www.last.fm/music/Official+HIGE+DANdism/_/Shukumei",
                "artist": {
                    "name": "Invalid Artist Link",
                    "url": "https://www.last.fm/music/Official+HIGE+DANdism"
                },
            }]
