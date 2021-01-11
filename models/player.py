import json


class Player:
    list_player = []

    def __init__(self, id, firstname, lastname, date_of_birth, sexe, rank):
        self.id = id
        self.first_name = firstname
        self.last_name = lastname
        self.date_of_birth = date_of_birth
        self.sexe = sexe
        self.rank = rank

    @classmethod
    def deserialize(cls, json_string):

        json_string = str(json_string).replace("\'", "\"")
        json_dict = json.loads(str(json_string))
        return cls(**json_dict)

    @classmethod
    def split_player(cls, list_player):
        liste = sorted(list_player, key=lambda player: player.rank, reverse=True)
        listeA = liste[0:4]
        listeB = liste[4:8]
        return listeA, listeB




