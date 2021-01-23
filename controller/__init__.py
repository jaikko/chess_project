from collections import OrderedDict

from models import menus, player, db, tournament, match, round
from view import HomeMenuView, PlayerMenuView, TournamentMenuView

menu = menus.Menu()
match = match
pl = player.Player
rnd = round


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
        self.ranking_end = {}


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

        # name = self.view.get_name()
        # while not name:
        #     name = self.view.get_name()
        # place = self.view.get_place()
        # while not place:
        #     place = self.view.get_place()
        # date = self.view.get_date()
        # while not date:
        #     date = self.view.get_date()
        # put = self.view.check_date()
        # while put == "o":
        #     date = self.view.get_date()
        #     while not date:
        #         date = self.view.get_date()
        #     put = self.view.check_date()
        # time = self.view.get_time()
        # while not time:
        #     time = self.view.get_time()
        # desc = self.view.get_desc()

        self.get_participant()
        liste_a, liste_b = pl.split_player(self.entrant)

        idtournament = db.get_id_tournament()
        print("generate match")

        for i in range(2):
            mm = match.Match()
            print(self.entrant)
            liste_a, liste_b = pl.split_player(self.entrant)
            for j in range(4):
                mm.add_match(liste_a[j],  0, liste_b[j], 0)
                self.list_match.append(mm.match)

            for row in self.list_match:
                p1 = row[0][0]
                p2 = row[1][0]
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
                self.ranking[i[0][0].player.id] = i[0][0].score
                self.ranking[i[1][0].player.id] = i[1][0].score

            print("classement")
            print(self.ranking)
            for k, v in sorted(self.ranking.items(), key=lambda x: x[1], reverse=True):
                self.ranking_bis[k] = v
            # for k in sorted(self.ranking.keys(), reverse=True):
            #     json = db.get_player_by_id(k)
            #     obj = pl.deserialize(json)
            #     self.ranking_bis[obj.id] = obj.rank
            #print("%s: %s" % (obj.id, self.ranking[k]))
            print(self.ranking_bis)
            all = []
            old_id = ""
            old_value = ""
            count = 0
            d2 = ""
            list_same = []
            dd = {}
            for k, v in self.ranking_bis.items():
                count += 1
                if k not in list_same:
                    if old_value == v:
                        list_same.append(k)
                        list_same.append(old_id)
                        if count == 8:
                            for i in list_same:
                                json = db.get_player_by_id(i)
                                obj = pl.deserialize(json)
                                dd[obj.rank] = obj.id
                                d2 = OrderedDict(sorted(dd.items(), key=lambda t: t[0], reverse=True))

                            for ke, va in d2.items():
                                all.append(va)
                            d2.clear()
                            dd.clear()
                            list_same.clear()
                    if old_value != v:

                        if len(list_same) > 1:
                            for i in list_same:
                                json = db.get_player_by_id(i)
                                obj = pl.deserialize(json)
                                dd[obj.rank] = obj.id
                                d2 = OrderedDict(sorted(dd.items(), key=lambda t: t[0], reverse=True))


                            for ke, va in d2.items():
                                all.append(va)
                            d2.clear()
                            dd.clear()
                            list_same.clear()
                old_id = k
                old_value = v

            print(all)
            self.entrant.clear()
            for s in all:
                json = db.get_player_by_id(s)
                obj = pl.deserialize(json)

                self.entrant.append(obj)

                print(f"id: {obj.id} nom: {obj.last_name} prenom: {obj.first_name} rank: {obj.rank}")
        print(self.entrant)
        rr = rnd.Round("Round 1", self.list_match)
        #print(rr.matchs)
        #print(self.ranking)
        # tr_obj = self.tr_obj(idtournament, name, place, desc, time)

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

