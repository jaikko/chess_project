import json


class Tournament:
    time = ["bullet", "blitz", "coup rapide"]

    def __init__(self, id, name, place, desc, time, laps=4, date=[], rounds="", player= []):
        self.name = name
        self.place = place
        self.date = date
        self.round = rounds
        self.players = player
        self.laps = laps
        self.time = time
        self.desc = desc
        self.id = id

    @staticmethod
    def deserialize(json_string):

        liste = []
        for i in json_string:
            json_string = str(i).replace("\'", "\"").strip('[]')
            json_dict = json.loads(str(json_string))
            liste.append(json_dict)

        return liste


