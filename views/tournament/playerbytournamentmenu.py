class PlayerByTournament:

    def __init__(self, menu):
        self.menu = menu

    def display_menu(self):
        print()
        for key, entry in self.menu.items():
            print(f"{key}: {entry.option}")
        print()

    def get_user_choice(self):
        print()
        self.display_menu()
        choice = input("Choisissez une action: ")
        return choice

    def return_controller(self, choice):
        return self.menu[choice]
