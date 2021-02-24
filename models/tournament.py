import json


class Tournament:
    time = ["bullet", "blitz", "coup rapide"]

    def __init__(self, id, name, place, desc, time, laps=4, date=[], round="", players=[]):
        self.name = name
        self.place = place
        self.date = date
        self.round = round
        self.players = players
        self.laps = laps
        self.time = time
        self.desc = desc
        self.id = id

    @classmethod
    def deserialize(cls, json_string):
        liste = []
        for i in json_string:
            json_string = str(i).replace("\'", "\"").strip('[]')
            json_dict = json.loads(str(json_string))
            liste.append(cls(**json_dict))
        return liste

    def __str__(self):
        return f" id: {str(self.id)} name: {self.name} place: {self.place} laps: {self.laps} " \
               f"date: {self.date if isinstance(self.date, list) == False  else ', '.join(self.date) }"
