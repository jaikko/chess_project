class AllTournamentView:

    def __init__(self, all):
        self.all = all

    def display_tournament(self):
        print()
        print("Liste des tournois")
        print()

        for i in self.all:

            for k, v in i.items():
                if k != "players":
                    if k != "round":
                        if v != "":
                            print(f"{k}: {v} ", end="")
            print()

    @staticmethod
    def quit():
        leave = input("Appuyer sur  entrée pour revenir au menu: ")
        return leave