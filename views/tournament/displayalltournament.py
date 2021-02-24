class DisplayAllTournament:

    def __init__(self, all):
        self.all = all

    def display_tournament(self):
        print()
        print("Liste des tournois")
        print()

        for i in self.all:
            print(i)

    @staticmethod
    def quit():
        print()
        leave = input("Appuyer sur  entrée pour revenir au menu: ")
        return leave
