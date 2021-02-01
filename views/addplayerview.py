class AddPlayerView:

    def __init__(self, player):
        self.player = player

    @staticmethod
    def get_firstname():
        first_name = input("prenom: ")
        return first_name

    @staticmethod
    def get_lastname():
        last_name = input(("nom: "))
        return last_name

    @staticmethod
    def get_dateofbirth():
        date_of_birth = input("date de naissance (dd/mm/yyyy): ")
        return date_of_birth

    @staticmethod
    def get_sexe():
        sexe = input(("sexe: "))
        return sexe

    @staticmethod
    def get_rank():
        rank = input("rang: ")
        return rank

    def add_player(self, id, lastname, firstname, date, sexe, rank):
        return self.player(id, firstname, lastname, date, sexe, rank)

    @staticmethod
    def quit():
        leave = input("Appuyer sur c pour ajouter un nouveau joueur ou entrée pour revenir au menu: ")
        return leave
