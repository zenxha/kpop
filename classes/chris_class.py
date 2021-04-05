import random

class song:
    def __init__(self, songs):
        if len(songs) < 0:
            raise ValueError("Songs must be greater than 0")
        self._songs = songs
        if not songs:
            self._songs = [{
                                "title": "Party Rock Anthem",
                                "link": "https://www.youtube.com/embed/KQ6zr6kCPj8",
                            },
                            {
                                "title": "Uptown Funk",
                                "link": "https://www.youtube.com/embed/OPf0YbXqDm0",
                            },
                            {
                                "title": "Wrecking Ball",
                                "link": "https://www.youtube.com/embed/My2FRPA3Gf8",
                            },
                            {
                                "title": "A Thousand Miles",
                                "link": "https://www.youtube.com/embed/Cwkej79U3ek",
                            }]

    def songshuffle(self):
        random.shuffle(self._songs)
        return self._songs