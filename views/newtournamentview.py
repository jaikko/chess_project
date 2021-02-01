class NewTournamentView:

    def __init__(self, players, time):
        self.players = players
        self.time = time

    def display_player(self):
        print("liste des joueurs")
        for pl in self.players:
            # print(f"id: {pl.id} prénom: {pl.first_name} nom: {pl.last_name} date de naissance: {pl.date_of_birth} "
            #       f" sexe: {pl.sexe} rank: {pl.rank}")
            print(pl)

    @staticmethod
    def get_id_choice():
        value = input("entrez l'id du joueur à ajouter: ")
        return value

    @staticmethod
    def error_id():
        print()
        print("saississez un nombre correct")

    @staticmethod
    def get_name():
        name = input("nom: ")
        return name

    @staticmethod
    def get_place():
        place = input("lieu: ")
        return place

    @staticmethod
    def get_date():
        date = input("date: ")

        return date
    @staticmethod
    def check_date():
        put = input("appuyer sur o pour ajouter une nouvelle date sinon n")
        return put

    def get_time(self):
        for i in self.time:
            print(i)
        time = input("contrôle du temps: ")
        return time

    @staticmethod
    def get_desc():
        desc = input("description: ")
        return desc

    @staticmethod
    def end_round():
        valide = input("Tour terminé? Appuyer sur entrée pour valider ")
        return valide

