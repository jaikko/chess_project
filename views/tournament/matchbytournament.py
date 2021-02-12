class MatchByTournament:

    def __init__(self, tr):
        self.tr = tr

    @staticmethod
    def display_match(matchs):

        print()
        print("Liste des matchs")
        print()
        print(matchs)
        for i in matchs:
            if i.s1 == 1:
                print(f"{i.p1.str()} a battu {i.p2.str()}  ")
            if i.s1 == 0.5:
                print(f"{i.p1.str()} et {i.p2.str()} se sont neutralisés  ")
            if i.s1 == 0:
                print(f"{i.p1.str()} a perdu contre {i.p2.str()}  ")

    @staticmethod
    def display_new_match(matchs):

        print()
        print(f" joueur 1: {matchs[0][0].str()} vs joueur 2: {matchs[1][0].str()} ")

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
        leave = input("Appuyer sur  entrée pour revenir au menu : ")
        return leave

    @staticmethod
    def left():
        print()
        leave = input("Appuyer sur  entrée pour revenir au menu  ou o pour continuer: ")
        return leave

    @staticmethod
    def display_rank_final(liste):
        print("classement final")
        for i in liste:
            print(i)