import copy
from collections import OrderedDict

from models import menus, player, db, tournament, match, round
from view import HomeMenuView, PlayerMenuView, TournamentMenuView

menu = menus.Menu()
match = match
pl = player.Player
rnd = round
tr = tournament


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
        put = self.view.quit()
        while put == "c":
            PlayerMenuController().__call__()
        HomeMenuController().__call__()


class TournamentMenuController:

    def __init__(self):
        self.players = None
        self.time = tournament.Tournament.time
        self.players_obj = []
        self.view = TournamentMenuView(self.players_obj, self.time)
        self.count = 0
        self.idplayer = []
        self.entrant = []
        self.tr_obj = tournament.Tournament
        self.list_match = []
        self.ranking = {}
        self.ranking_bis = {}
        self.list_round = None
        self.list_ordered = {}
        self.list_obj_round = []

    def __call__(self):
        print("tournoi")
        self.players = db.get_all_player()
        self.get_object_display()
        while self.count <= 7:
            self.view.display_player()
            choice = self.view.get_id_choice()

            while not choice.isdigit():
                choice = self.view.get_id_choice()

            while choice in self.idplayer:
                print("error")
                choice = self.view.get_id_choice()

            self.idplayer.append(choice)

            self.count += 1

        name = self.view.get_name()
        while not name:
            name = self.view.get_name()
        place = self.view.get_place()
        while not place:
            place = self.view.get_place()
        date = self.view.get_date()
        while not date:
            date = self.view.get_date()
        put = self.view.check_date()
        while put == "o":
            date = self.view.get_date()
            while not date:
                date = self.view.get_date()
            put = self.view.check_date()
        time = self.view.get_time()
        while not time:
            time = self.view.get_time()
        desc = self.view.get_desc()

        self.get_participant()

        idtournament = db.get_id_tournament()
        print("generate match")
        # boucle pour les rounds
        for num in range(3):
            mm = match.Match()
            self.list_match.clear()
            ll = ""

            if num == 0:
                liste_a, liste_b = pl.split_player_by_rank(self.entrant)
                for h in range(4):
                    mm.add_match(liste_a[h], 0, liste_b[h], 0)

                    self.list_match.append(mm.match)
            else:

                liste_order = pl.ranking_by_score(self.ranking_bis)
                val = pl.check_same_score(liste_order)
                if val:
                    liste_order = pl.ranking_by_rank(liste_order)

                for j in range(0, 7, 2):
                    ll = pl.return_list_object(liste_order)
                    mm.add_match(ll[j], 0, ll[j + 1], 0)
                    self.list_match.append(mm.match)
                print(self.list_match)
                # vérification des matchs
                print(liste_order)

                for ad in self.list_round:

                    p1 = ad[0].player.id
                    p2 = ad[1].player.id
                    if mm.match[0].player.id == p1 and mm.match[1].player.id == p2:
                        print("same")
                        self.list_match.clear()
                        mm.add_match(ll[0], 0, ll[2], 0)
                        self.list_match.append(mm.match)
                        mm.add_match(ll[1], 0, ll[3], 0)
                        self.list_match.append(mm.match)
                        mm.add_match(ll[4], 0, ll[5], 0)
                        self.list_match.append(mm.match)
                        mm.add_match(ll[6], 0, ll[7], 0)
                        self.list_match.append(mm.match)

            for row in self.list_match:
                p1 = row[0]
                p2 = row[1]
                print("row")
                print(p1.items())
                print(p2.items())

                winner = input("gagnant(numéro du joueur): ")
                if winner == "1":
                    p1.score += 1
                elif winner == "2":
                    p2.score += 1

                elif not winner:
                    p1.score += 0.5
                    p2.score += 0.5

            for i in self.list_match:
                self.ranking[i[0].player.id] = i[0].score
                self.ranking[i[1].player.id] = i[1].score

            if num == 0:
                self.ranking_bis = self.ranking.copy()
            else:

                for k, v in self.ranking.items():
                    for key, val in self.ranking_bis.items():

                        if k == key:
                            value = val + v

                            self.ranking_bis[k] = value

            rr = rnd.Round("round " + str(num + 1), self.list_match)
            self.list_obj_round.append(rr)
            self.list_round = rr.matchs.copy()

        tr.Tournament(idtournament, name, place, desc, time, "", date, self.list_obj_round, self.entrant)
        print("classement")
        print(f" bis {self.ranking_bis}")
        #affichage classement
        liste_order = pl.ranking_by_score(self.ranking_bis)
        val = pl.check_same_score(liste_order)
        if val:
            liste_order = pl.ranking_by_rank(liste_order)

        ll = pl.return_list_object(liste_order)

        for pla in ll:
            print(pla)

        # tr_serialize = db.tournament_db(tr_obj)
        # db.add_tournament_db(tr_serialize)

        # db.update_playerslist(self.idplayer, idtournament)

    # convertir en objet pour l'affichage
    def get_object_display(self):
        for i in self.players:
            player_obj = pl.deserialize(i)
            self.players_obj.append(player_obj)

    def get_participant(self):
        for i in self.idplayer:
            json = db.get_player_by_id(i)
            play = pl.deserialize(json)

            self.entrant.append(play)
