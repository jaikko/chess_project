from models import player


class MatchEntry1:
    def __init__(self, player, score=0):
        self.player = player
        self.score = score

    def items(self):
        return f"Joueur 1: {self.player.firstname} {self.player.lastname}({self.player.id})"


class MatchEntry2:
    def __init__(self, player, score=0):
        self.player = player
        self.score = score

    def items(self):
        return f"Joueur 2: {self.player.firstname} {self.player.lastname}({self.player.id})"


class Match:

    def __init__(self, match=(), all_match=[]):
        self.match = match
        self.matchs = all_match

    def add_match(self, player1, score1, player2, score2):
        self.match = MatchEntry1(player1, score1), MatchEntry2(player2, score2)

    def matchs(self, match):
        self.matchs = [match]

    def items(self):
        return self.match.items()

    def return_match(self):
        return f"Joueur 1: {self.match[0].player.first_name} "

    @staticmethod
    def check_match(liste, new_liste):
        pass

    def return_list_obj(self, liste):

        pl1 = ""
        pl2 = ""
        score1 = ""
        score2 = ""
        count = 0
        liste_obj = []
        for g in liste:

            for f in g:
                count += 1
                if count == 1:

                    for k, v in f.items():
                        if k == "player":
                            pl1 = player.Player.deserialize(v)
                        if k == "score":
                            score1 = v
                if count == 2:

                    for k, v in f.items():
                        if k == "player":
                            pl2 = player.Player.deserialize(v)
                        if k == "score":
                            score2 = v

            Match.add_match(self, pl1, score1, pl2, score2)
            liste_obj.append(self.match)
            count = 0
        return liste_obj
