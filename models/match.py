class Match:

    list_match = []

    def __init__(self, player, opponent, result_player="", result_opponent=""):
        self.player = player
        self.opponent = opponent
        self.result_player = result_player
        self.result_opponent = result_opponent

    def __str__(self):
        return str(self.player, self.opponent)

    @classmethod
    def generate_match(cls, l1, l2):
        matchs = []
        for i in range(3):
            match = Match(l1[i], l2[i])
            matchs.append(match)

        return matchs





