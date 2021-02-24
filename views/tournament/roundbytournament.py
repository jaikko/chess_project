class RoundByTournamentView:

    def __init__(self, tr):
        self.tr = tr

    @staticmethod
    def display_round(rnd):

        print("Liste des rounds")
        print()
        for i in rnd:
            print()
            print(f"{i.name}")
            print()
            for j in i.matchs:

                if j.s1 == 1:
                    print(f"{j.p1.str()} a battu {j.p2.str()}  ")
                if j.s1 == 0.5:
                    print(f"{j.p1.str()} et {j.p2.str()} se sont neutralisés  ")
                if j.s1 == 0:
                    print(f"{j.p1.str()} a perdu contre {j.p2.str()}  ")

    def display_tournament(self):
        print()
        print("Liste des tournois")
        print()

        for i in self.tr:
            print(i)

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
