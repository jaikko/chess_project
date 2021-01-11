from views import HomeMenuView, PlayerMenuView, TournamentMenuView
from models import menus, db, player, match

menu = menus.Menu()
db = db.Db()
pl = player.Player
match = match.Match


class ApplicationController:
    def __init__(self):
        self.controller = None

    def start(self):
        self.controller = HomeMenuController()
        self.controller.__call__()


class PlayerMenuController:
    def __init__(self):
        self.menu = menu
        self.view = PlayerMenuView(self.menu)

    def __call__(self):
        player_str = self.view.add_player()
        player.id = db.get_id_player()
        serialize_player = db.serialize_player(player_str)
        db.add_db(serialize_player)
        leave = self.view.quit()
        if leave == "c":
            PlayerMenuController()
            PlayerMenuController().__call__()
        if leave == "q":
            ApplicationController().start()


class HomeMenuController:
    def __init__(self):
        self.menu = menu
        self.view = HomeMenuView(self.menu)

    def __call__(self):
        self.menu.add("1", "ajouter joueur", PlayerMenuController())
        self.menu.add("2", "créer un tournoi", TournamentMenuController())
        user_choice = self.view.get_user_choice()
        while user_choice == "error":
            self.view.error()
            user_choice = self.view.get_user_choice()

        user_choice.controller()
        # controller = menu.__getitem__(user_choice)[1]
        # print((str(controller)))
        # if user_choice == "1":
        #      PlayerMenuController()
        #      PlayerMenuController().__call__()


class TournamentMenuController:

    def __init__(self):
        self.menu = match
        self.view = TournamentMenuView(self.menu)

    def __call__(self):
        self.count = 0
        self.liste = []
        self.idtournament = db.get_id_tournament()

        while self.count <= 7:
            db.show_player()
            idplayer = self.view.add_player_to_tournament()
            player_info = db.get_player_by_id(int(idplayer))
            db.player_by_tournament(self.idtournament, idplayer)
            player_info = pl.deserialize(player_info[0])
            self.liste.append(player_info)
            self.count += 1

        liste_a, liste_b = pl.split_player(self.liste)
        matchs = match.generate_match(liste_a, liste_b)
        for i in matchs:
            print(str(i.player.first_name) + "vs" + str(i.opponent.first_name))
