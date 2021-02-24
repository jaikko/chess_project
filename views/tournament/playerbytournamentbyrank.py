class PlayerByTournamentByRank:

    def __init__(self, tr, players):
        self.players = players
        self.tr = tr

    def display_player(self):
        print("Liste des joueurs")
        print("")
        for i in self.players:
            print(i)

    def display_tournament(self):
        print()
        print("Liste des tournois")
        print()

        for i in self.tr:
            print(i)

    @staticmethod
    def get_user_choice():
        print("")
        put = input("Entrez id du tournoi: ")
        return put

    @staticmethod
    def quit():
        print("")
        leave = input("Appuyer entrée pour quitter: ")
        return leave
