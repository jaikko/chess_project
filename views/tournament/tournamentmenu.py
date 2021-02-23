class TournamentMenuView:

    def __init__(self, menu):
        self.menu = menu

    def display_menu(self):
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
