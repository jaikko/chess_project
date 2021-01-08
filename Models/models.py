



class Player:
    list_player = []

    def __init__(self, id, first_name, last_name, date_of_birth, sexe, rank):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.sexe = sexe
        self.rank = rank


class Match:
    def __init__(self, player, opponent, result_player="", result_opponent=""):
        self.player = player
        self.opponent = opponent
        self.result_player = result_player
        self.result_opponent = result_opponent


class Round:

    def __init__(self, name, obj=Match):
        self.name = name
        self.match = obj

class Tournament:


    def __init__(self, name, place, date, obj = Round):
        self.name = name
        self.place = place
        self.date = date
        self.match = obj