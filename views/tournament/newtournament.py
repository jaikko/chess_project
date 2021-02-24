class NewTournamentView:

    def __init__(self, players, time):
        self.players = players
        self.time = time

    def display_player(self):
        print()
        print("liste des joueurs")
        print()
        for pl in self.players:
            print(pl)
        print()

    @staticmethod
    def get_id_choice():
        value = input("entrez l'id du joueur à ajouter: ")
        return value

    @staticmethod
    def error_id():
        print()
        print("Joueur déjà ajouté, saisir un autre id")

    @staticmethod
    def error_id_availible():
        print()
        print("Id introuvable, saisir un nouveau")

    @staticmethod
    def get_name():
        print()
        name = input("nom: ")
        return name

    @staticmethod
    def get_place():
        print()
        place = input("lieu: ")
        return place

    @staticmethod
    def get_date():
        print()
        date = input("date: ")
        return date

    @staticmethod
    def check_date():
        put = input("appuyer sur o pour ajouter une nouvelle date sinon entrée")
        return put

    def show_time(self):
        print()
        for i in self.time:
            print(i)

    @staticmethod
    def get_time():
        time = input("contrôle du temps: ")
        return time

    @staticmethod
    def get_desc():
        print()
        desc = input("description(appuyez sur entrée si vide): ")
        return desc

    @staticmethod
    def end_round():
        print()
        valide = input("Tour terminé? Appuyer sur entrée pour valider ")
        return valide

    @staticmethod
    def same_rank():
        print()
        return print('Vous avez deux joueurs avec le même classement, modifier les classements identiques')

    @staticmethod
    def quit():
        print("")
        leave = input("Appuyer entrée pour quitter: ")
        return leave
