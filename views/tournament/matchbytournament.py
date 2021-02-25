class MatchByTournament:

    def __init__(self, tr):
        self.tr = tr

    @staticmethod
    def display_match(matchs):

        print()
        print("Liste des matchs")
        print()
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
            print(i)

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
    def end_round():
        print()
        enter = input("Appuyer sur  entrée pour valider le round: ")
        return enter

    @staticmethod
    def left():
        print()
        leave = input("Appuyer sur  entrée pour revenir au menu  ou o pour continuer: ")
        return leave

    @staticmethod
    def display_rank_final(liste, score):
        print("classement final")
        print()
        for i in liste:
            for k, v in score.items():
                if k == i.id:
                    print(f" {i} avec {v} points")

    @staticmethod
    def choice_edit_player():
        print()
        choice = input("Appuyer sur  entrée pour revenir au menu ou saisissez o pour modifier classement: ")
        return choice

    @staticmethod
    def display_player(player):
        print()
        for i in player:
            print(i)

    @staticmethod
    def edit_player_id():
        print()
        choice = input("entrez id du joueur à modifier: ")
        return choice

    @staticmethod
    def change_value():
        rank = input("entrez son nouveau classement:")
        return rank

    @staticmethod
    def display_player_choice(player):
        return print(player)

    @staticmethod
    def left_edit():
        print()
        leave = input("Appuyer sur  entrée pour revenir au menu ou saisissez o pour modifier classement: ")
        return leave

    @staticmethod
    def get_winner():
        print()
        win = input("gagnant(numéro du joueur) si match nul appuyez sur entrée: ")
        return win

    @staticmethod
    def display_num_round(num):
        print()
        print(f" round {num}")
