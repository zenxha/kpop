import random


class top_5:
    def __init__(self, tracks):
        if len(tracks) < 0:
            raise ValueError("Songs must be greater than 0")
        self._tracks = tracks
        if not tracks:
            self._tracks = [{
                    "title": "Mirrors by Jason Richardson",
                    "link": "https://www.youtube.com/embed/Utj1VuJE7V0",
                },
                {
                    "title": "A Cruel Angel's Thesis",
                    "link": "https://www.youtube.com/embed/k8ozVkIkr-g",
                },
                {
                    "title": "505 by Arctic Monkeys",
                    "link": "https://www.youtube.com/embed/My2FRPA3Gf8",
                },
                {
                    "title": "More Than A Woman by The Bee Gees",
                    "link": "https://www.youtube.com/embed/zwyKQnbDJRg",
                },
                {
                    "title": "Billie Jean by Michael Jackson",
                    "link": "https://www.youtube.com/embed/Zi_XLOBDo_Y"
                }]

    def trackshuffle(self):
        random.shuffle(self._tracks)
        return self._tracks