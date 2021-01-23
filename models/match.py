class MatchEntry1:
    def __init__(self, player, score=0):
        self.player = player
        self.score = score

    def items(self):
        return f"Joueur 1: {self.player.first_name} {self.player.last_name}({self.player.id})   "

    def __str__(self):
        return f"Joueur 1: {self.player.first_name} {self.player.last_name}({self.player.id}) {self.score}  "


class MatchEntry2:
    def __init__(self, player, score=0):
        self.player = player
        self.score = score

    def items(self):
        return f"Joueur 2: {self.player.first_name} {self.player.last_name}({self.player.id}) vs  "

    def __str__(self):
        return f"Joueur 2: {self.player.first_name} {self.player.last_name} ({self.player.id}) {self.score}"


class Match:

    def __init__(self, match=(), all_match=[]):
        self.match = match
        self.matchs = all_match

    def add_match(self, player1, score1, player2, score2):
        self.match = [MatchEntry1(player1, score1)], [MatchEntry2(player2, score2)]

    def matchs(self, match):
        self.matchs = [match]

    def items(self):
        return self.match.items()

    def return_match(self):
        return f"Joueur 1: {self.match[0].player.first_name} "

