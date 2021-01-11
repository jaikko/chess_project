from models import player


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
        while True:
            self.display_menu()
            choice = input("choisir une action: ")

            if choice in self.menu:
                return self.menu[choice]
            else:
                return "error"

    def display_error(self):
        print()
        print("Veuilez saisir un chiffre correcte")


class PlayerMenuView:

    def __init__(self, menu):
        self.menu = menu

    def add_player(self):
        first_name = input("prenom: ")
        last_name = input(("nom: "))
        date_of_birth = input("date de naissance: ")
        sexe = input(("sexe: "))
        rank = input("rang: ")
        return player.Player("", first_name, last_name, date_of_birth, sexe, rank)

    def quit(self):
        leave = input("Appuyer sur c pour ajouter un nouveau joueur ou q pour revenir au menu: ")
        return leave


class TournamentMenuView:

    def __init__(self, match):
        self.match = match

    def add_player_to_tournament(self):
        value = input("entrez l'id du joueur à ajouter")
        return value
    def display_match(self):
        self.match.


