class RoundByTournamentView:

    def __init__(self, tr):
        self.tr = tr

    @staticmethod
    def display_round(rnd):

        print()
        print("Liste des rounds")
        print()
        for k, v in rnd.items():
            print()
            print(f"{k}:")
            print()
            for i in v:
                if i[0].score == 1:
                    print(f"{i[0].player.str()} a battu {i[1].player.str()}  ")
                if i[0].score == 0.5:
                    print(f"{i[0].player.str()} et {i[1].player.str()} se sont neutralisés  ")
                if i[0].score == 0:
                    print(f"{i[0].player.str()} a perdu contre {i[1].player.str()}  ")

    def display_tournament(self):
        print()
        print("Liste des tournois")
        print()

        for i in self.tr:

            for k, v in i.items():
                if k != "players":
                    if k != "round":
                        if v != "":
                            print(f"{k}: {v} ", end="")
            print()

    @staticmethod
    def get_user_choice():
        print()
        put = input("entrez id d'un tournoi: ")
        return put

    @staticmethod
    def quit():
        print()
        leave = input("Appuyer sur  entrée pour revenir au menu: ")
        return leave