from models import menus, player, db
from view import HomeMenuView, PlayerMenuView, TournamentMenuView

menu = menus.Menu()
pl = player.Player


class ApplicationController:
    def __init__(self):
        self.controller = None

    def start(self):
        self.controller = HomeMenuController()
        self.controller.__call__()


class HomeMenuController:
    def __init__(self):
        self.menu = menu
        self.view = HomeMenuView(self.menu)

    def __call__(self):
        self.menu.add("1", "ajouter joueur", PlayerMenuController())
        self.menu.add("2", "créer un tournoi", TournamentMenuController())
        user_choice = self.view.get_user_choice()
        check = self.menu.__contains__(user_choice)
        check = eval(check)

        while not check:
            self.view.display_error()
            user_choice = self.view.get_user_choice()
            check = self.menu.__contains__(user_choice)

        user_choice = self.view.return_controller(user_choice)
        user_choice.controller()


class PlayerMenuController:

    def __init__(self):
        self.menu = player
        self.view = PlayerMenuView(self.menu)

    def __call__(self):
        firstname = self.view.get_firstname()
        while not firstname:
            firstname = self.view.get_firstname()
        lastname = self.view.get_lastname()
        while not lastname:
            lastname = self.view.get_lastname()
        date_of_birth = self.view.get_dateofbirth()
        while not date_of_birth:
            date_of_birth = self.view.get_dateofbirth()
        sexe = self.view.get_sexe()
        while not sexe.isalpha():
            sexe = self.view.get_sexe()
        rank = self.view.get_rank()
        while not rank.isdigit():
            rank = self.view.get_rank()

        id = db.get_id_player()
        player_obj = self.view.add_player(id, lastname, firstname, date_of_birth, sexe, rank)
        player_json = db.serialize_player(player_obj)
        db.add_db(player_json)


class TournamentMenuController:

    def __init__(self):
        self.players = None
        self.players_obj = []
        self.view = TournamentMenuView(self.players_obj)
        self.count = 0

    def __call__(self):
        print("tournoi")
        idtournament = db.get_id_tournament()
        self.players = db.get_all_player()
        self.get_object()
        while self.count <= 1:
            self.view.display_player()
            choice = self.view.get_id_choice()
            while not choice.isdigit():
                choice = self.view.get_id_choice()
            row = db.check_idplayer_tournament(idtournament, choice)
            print(row)
            while row > 0:
                print("error")
                choice = self.view.get_id_choice()
                row = db.check_idplayer_tournament(idtournament, choice)
            db.player_by_tournament(idtournament, int(choice))
            self.count += 1

    def get_object(self):
        for i in self.players:
            player_obj = pl.deserialize(i)
            self.players_obj.append(player_obj)
