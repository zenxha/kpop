

class games:
    def __init__(self, games):
        if len(games) < 0:
            raise ValueError("Songs must be greater than 0")
        self._games = games
        if not games:
            self._games = [{
                "title": "ARK: Survival Evolved",
                "releasedate": "June 2, 2015",
                "randomfact": "The game was designed by Kayd Hendricks.",

            },
                {
                    "title": "Risk of Rain 2",
                    "releasedate": "March 28, 2019",
                    "randomfact": "It's a roguelike third-person shooter developed by Hopoo Games",
                },
                {
                    "title": "The Binding of Isaac",
                    "releasedate": "September 28, 2011",
                    "randomfact": "The game was the result of a week-long game jam between McMillen and Himsl to develop a The Legend of Zelda-inspired roguelike",
                },
                {
                    "title": "Minecraft",
                    "releasedate": "November 18, 2011",
                    "randomfact": "The game was created by Markus Notch",
                }]

    def calculateage(self):

    def getgames(self):
        return self._games
