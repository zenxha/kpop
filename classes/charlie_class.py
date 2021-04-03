import datetime

class game:
    def __init__(self, title,releasedate,randomfact=None):
        self._title = title
        self._releasedate = releasedate
        self._randomfact = randomfact

    def calculateage(self):
        release_obj = datetime.datetime.strptime(self._releasedate, '%Y-%m-%d')
        diff = datetime.datetime.now() - release_obj
        return diff
    def gettitle(self):
        return self._title
    def getreleasedate(self):
        return self._releasedate
    def getrandomfact(self):
        return self._randomfact