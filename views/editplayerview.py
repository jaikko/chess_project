class EditPlayerView:

    def __init__(self, player):
        self.player = player

    def display_player(self):
        for i in self.player:
            print(i)

    def get_user_choice(self):
        print()

        self.display_player()
        choice = input("Choississez un id: ")
        return choice

    @staticmethod
    def change_value():
        rank = input("entrez son nouveau classement")
        return rank

    @staticmethod
    def display_player_choice(player):
        return print(player)

