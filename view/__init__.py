class HomeMenuView:

    def __init__(self, menu):
        self.menu = menu

    def display_menu(self):
        print("Bienvenue:")
        for key, entry in self.menu.items():
            print(f"{key}: {entry.option}")
        print("")

    def get_user_choice(self):
        print()

        self.display_menu()
        choice = input("Choississez une action: ")
        return choice

    def return_controller(self, choice):
        return self.menu[choice]

    @staticmethod
    def display_error():
        print()
        print("Veuilez saisir un chiffre correcte")


class PlayerMenuView:

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
        return self.player.Player(id, firstname, lastname, date, sexe, rank)

    @staticmethod
    def quit():
        leave = input("Appuyer sur c pour ajouter un nouveau joueur ou q pour revenir au menu: ")
        return leave


class TournamentMenuView:

    def __init__(self, players):
        self.players = players

    def display_player(self):
        print("liste des joueurs")
        for pl in self.players:
            print(f"id: {pl.id} prénom: {pl.first_name} nom: {pl.last_name} date de naissance: {pl.date_of_birth} "
                  f" sexe: {pl.sexe} rank: {pl.rank}")

    @staticmethod
    def get_id_choice():
        value = input("entrez l'id du joueur à ajouter: ")
        return value

    @staticmethod
    def error_id():
        print()
        print("saississez un nombre correct")

