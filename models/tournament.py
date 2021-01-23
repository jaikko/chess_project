

class Tournament:
    time = ["bullet", "blitz", "coup rapide"]

    def __init__(self, id, name, place,desc, time, laps=4, date=[], rounds=[], player=""):
        self.name = name
        self.place = place
        self.date = date
        self.round = rounds
        self.players = player
        self.laps = laps
        self.time = time
        self.desc = desc
        self.id = id
