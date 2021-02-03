class PlayerOrderByNameView:

    def __init__(self, players):
        self.players = players

    def display_player(self):
        print("")
        for i in self.players:
            print(i)

    @staticmethod
    def quit():
        print("")
        leave = input("Appuyer entrée pour quitter: ")
        return leave


