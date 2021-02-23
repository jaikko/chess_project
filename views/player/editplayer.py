class EditPlayerView:

    def __init__(self, player):
        self.player = player

    def display_player(self):
        print()
        for i in self.player:
            print(i)

    @staticmethod
    def get_user_choice():
        print()
        choice = input("Choississez un id: ")
        return choice

    @staticmethod
    def change_value():
        rank = input("entrez son nouveau classement:")
        return rank

    @staticmethod
    def display_player_choice(player):
        return print(player)

    @staticmethod
    def left():
        print()
        leave = input("Appuyer sur  entrée pour revenir au menu: ")
        return leave
