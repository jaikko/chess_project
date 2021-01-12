class Match:

    def __init__(self, player, opponent, result_player="", result_opponent=""):
        self.player = player
        self.opponent = opponent
        self.result_player = result_player
        self.result_opponent = result_opponent

    def __str__(self):
        return str(self.player, self.opponent)