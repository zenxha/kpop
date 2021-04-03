class eshaan_top_5:
    def __init__(self, tracks):
        if len(tracks) < 0:
            raise ValueError("Trackss must be greater than 0")
        self._tracks = tracks
        if not tracks:
            self._tracks = [{
                                "title": "Mirrors By Jason Richardson",
                                "link": "https://www.youtube.com/embed/Utj1VuJE7V0",
                            },
                            {
                                "title": "A Cruel Angel's Thesis by Shiro Sagisu",
                                "link": "https://www.youtube.com/embed/OPf0YbXqDm0",
                            },
                            {
                                "title": "505 by Arctic Monkeys",
                                "link": "https://www.youtube.com/embed/MrmPDUvKyLs",
                            },
                            {
                                "title": "More Than A Woman by The Bee Gees",
                                "link": "https://www.youtube.com/embed/zwyKQnbDJRg",
                            },
                            {
                                "title": "Billie Jean by Michael Jackson",
                                "link": "https://www.youtube.com/embed/Zi_XLOBDo_Y",
                            }]
