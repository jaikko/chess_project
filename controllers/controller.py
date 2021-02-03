from datetime import datetime
import jsons as jsons

from models import menu, player, db, match, tournament, round
from views import homemenuview, playermenuview, tournamentmenuview, addplayerview, editplayerview, \
    playerorderbynameview, playerorderbyrankview, newtournamentview, alltournamentview, menuplayerbytournamentview \
    , playerbytournamentbynameview, playerbytournamentbyrankview, matchbytournamentview, roundbytournamentview

menu = menu.Menu()
player = player.Player
match = match
rnd = round
tr = tournament


class ApplicationController:
    def __init__(self):
        self.controller = None

    def start(self):
        self.controller = HomeMenuController()
        self.controller.__call__()


# Menu principal
class HomeMenuController:
    def __init__(self):
        self.menu = menu
        self.view = homemenuview.HomeMenuView(self.menu)

    def __call__(self):
        self.menu.clear()
        self.menu.add("1", "Gestion des joueurs", PlayerMenuController())
        self.menu.add("2", "Gestion des tournois", TournamentMenuController())
        user_choice = self.view.get_user_choice()
        check = self.menu.__contains__(user_choice)
        check = eval(check)

        while not check:
            self.view.display_error()
            user_choice = self.view.get_user_choice()
            check = self.menu.__contains__(user_choice)

        user_choice = self.view.return_controller(user_choice)
        user_choice.controller()


# Menu Joueur
class PlayerMenuController:
    def __init__(self):
        self.menu = menu
        self.view = playermenuview.PlayerMenuView(self.menu)

    def __call__(self):
        self.menu.add("1", "Ajouter des joueurs", AddPlayerController())
        self.menu.add("2", "Modifier un joueur", EditPlayerController())
        self.menu.add("3", "Liste de tous les acteurs", PlayerController())
        self.menu.add("4", "Retour", HomeMenuController())
        user_choice = self.view.get_user_choice()
        check = self.menu.__contains__(user_choice)
        check = eval(check)

        while not check:
            self.view.display_error()
            user_choice = self.view.get_user_choice()
            check = self.menu.__contains__(user_choice)

        user_choice = self.view.return_controller(user_choice)
        user_choice.controller()


# Menu pour choisir choix du trie des joueurs
class PlayerController:
    def __init__(self):
        self.menu = menu
        self.view = playermenuview.PlayerMenuView(self.menu)

    def __call__(self):
        self.menu.clear()
        self.menu.add("1", "Trier par ordre alphabétique", PlayerOrderByName())
        self.menu.add("2", "Trier par classement", PlayerOrderByRank())
        self.menu.add("3", "Retour", PlayerMenuController())
        user_choice = self.view.get_user_choice()
        check = self.menu.__contains__(user_choice)
        check = eval(check)

        while not check:
            self.view.display_error()
            user_choice = self.view.get_user_choice()
            check = self.menu.__contains__(user_choice)

        user_choice = self.view.return_controller(user_choice)
        user_choice.controller()


# Lister joueur par Nom
class PlayerOrderByName:
    def __init__(self):
        self.players = db.get_all_player()
        self.players = player.return_list_object_from_list(self.players)
        self.players.sort(key=lambda p: p.lastname, reverse=False)

        self.view = playerorderbynameview.PlayerOrderByNameView(self.players)

    def __call__(self):
        self.view.display_player()
        put = self.view.quit()

        while put != "":
            put = self.view.quit()

        PlayerController().__call__()


# Lister joueur par classement
class PlayerOrderByRank:
    def __init__(self):
        self.players = db.get_all_player()
        self.players = player.return_list_object_from_list(self.players)
        self.players.sort(key=lambda p: p.rank, reverse=False)

        self.view = playerorderbyrankview.PlayerOrderByNameView(self.players)

    def __call__(self):
        self.view.display_player()
        put = self.view.quit()

        while put != "":
            put = self.view.quit()

        PlayerController().__call__()


# Ajouter joueur
class AddPlayerController:
    def __init__(self):
        self.player = player
        self.view = addplayerview.AddPlayerView(self.player)

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
            AddPlayerController().__call__()

        PlayerMenuController().__call__()


# Modifier rank d'un joueur
class EditPlayerController:
    def __init__(self):
        self.player = []
        self.player = db.get_all_player()
        self.player = player.return_list_object_from_list(self.player)
        self.view = editplayerview.EditPlayerView(self.player)

    def __call__(self):
        self.view.display_player()
        id = self.view.get_user_choice()
        max = db.get_max_id()
        while not id.isdigit():
            id = self.view.get_user_choice()

        while int(id) > int(max):
            self.view.error_id_availible()
            id = self.view.get_user_choice()
        json = db.get_player_by_id(id)
        p = player.deserialize(json)
        self.view.display_player_choice(p)
        rank = self.view.change_value()
        db.update_player_rank(id, rank)


# Menu Tournoi
class TournamentMenuController:
    def __init__(self):
        self.menu = menu
        self.view = tournamentmenuview.TournamentMenuView(self.menu)

    def __call__(self):
        self.menu.clear()
        self.menu.add("1", "Créer un tournoi", NewTournamentController())
        self.menu.add("2", "Liste de tous les tournois", DisplayTournamentController())
        self.menu.add("3", "Liste de tous les tours d'un tournoi", RoundByTournamentController())
        self.menu.add("4", "Liste de tous les matchs d'un tournoi", MatchByTournament())
        self.menu.add("5", "Liste de tous les joueurs d'un tournoi", MenuPlayerByTournamentController())
        self.menu.add("6", "Retour", HomeMenuController())
        user_choice = self.view.get_user_choice()
        check = self.menu.__contains__(user_choice)
        check = eval(check)

        while not check:
            self.view.display_error()
            user_choice = self.view.get_user_choice()
            check = self.menu.__contains__(user_choice)

        user_choice = self.view.return_controller(user_choice)
        user_choice.controller()


# Créer un nouveau tournoi
class NewTournamentController:
    def __init__(self):
        self.players = None
        self.time = tournament.Tournament.time
        self.players_obj = []
        self.view = newtournamentview.NewTournamentView(self.players_obj, self.time)
        self.count = 0
        self.idplayer = []
        self.entrant = []
        self.tr_obj = tournament.Tournament
        self.list_match = []
        self.ranking = {}
        self.ranking_bis = {}
        self.list_round = []
        self.list_ordered = {}
        self.list_obj_round = []
        self.list_player_json = []
        self.list_round_json = []

    def __call__(self):
        print("tournoi")
        self.players = db.get_all_player()
        self.get_object_display()
        max = db.get_max_id()

        while self.count <= 7:
            self.view.display_player()
            choice = self.view.get_id_choice()

            while not choice.isdigit():
                choice = self.view.get_id_choice()

            while int(choice) > int(max):
                self.view.error_id_availible()
                choice = self.view.get_id_choice()

            while choice in self.idplayer:
                self.view.error_id()
                choice = self.view.get_id_choice()
                while int(choice) > int(max):
                    self.view.error_id_availible()
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
        print("generation des matchs")
        print()
        # boucle pour les rounds
        for num in range(4):
            mm = match.Match()
            self.list_match.clear()
            ll = ""
            # génération de la date
            date = datetime.today().strftime('%d-%m-%Y')
            # génération de l'heure de début
            date_start = datetime.today().strftime('%H:%M')

            if num == 0:
                liste_a, liste_b = player.split_player_by_rank(self.entrant)
                for h in range(4):
                    mm.add_match(liste_a[h], 0, liste_b[h], 0)

                    self.list_match.append(mm.match)
            else:

                liste_order = player.ranking_by_score(self.ranking_bis)
                val = player.check_same_score(liste_order)
                if val:
                    liste_order = player.ranking_by_rank(liste_order)
                    print(f"ls{liste_order}")

                for j in range(0, 7, 2):
                    ll = player.return_list_object_from_dict(liste_order)

                    mm.add_match(ll[j], 0, ll[j + 1], 0)
                    self.list_match.append(mm.match)

                # vérification des matchs
                cc = 0

                for ad in self.list_round:
                    cc += 1
                    p1 = ad[0].player.id
                    p2 = ad[1].player.id
                    for row in self.list_match:

                        if row[0].player.id == p1 and row[1].player.id == p2 or row[0].player.id == p2 \
                                and row[1].player.id == p1:

                            if cc in [1, 5, 9]:

                                self.list_match.clear()
                                mm.add_match(ll[0], 0, ll[2], 0)
                                self.list_match.append(mm.match)
                                mm.add_match(ll[1], 0, ll[3], 0)
                                self.list_match.append(mm.match)
                                mm.add_match(ll[4], 0, ll[5], 0)
                                self.list_match.append(mm.match)
                                mm.add_match(ll[6], 0, ll[7], 0)
                                self.list_match.append(mm.match)

                                for a in self.list_round:

                                    p1 = a[0].player.id
                                    p2 = a[1].player.id
                                    for rows in self.list_match:
                                        if rows[0].player.id == p1 and rows[1].player.id == p2 or rows[
                                            0].player.id == p2 \
                                                and rows[1].player.id == p1:
                                            self.list_match.clear()
                                            mm.add_match(ll[0], 0, ll[4], 0)
                                            self.list_match.append(mm.match)
                                            mm.add_match(ll[2], 0, ll[1], 0)
                                            self.list_match.append(mm.match)
                                            mm.add_match(ll[3], 0, ll[7], 0)
                                            self.list_match.append(mm.match)
                                            mm.add_match(ll[5], 0, ll[6], 0)
                                            self.list_match.append(mm.match)

                            if cc in [4, 8, 12]:
                                self.list_match.clear()
                                mm.add_match(ll[0], 0, ll[4], 0)
                                self.list_match.append(mm.match)
                                mm.add_match(ll[2], 0, ll[1], 0)
                                self.list_match.append(mm.match)
                                mm.add_match(ll[3], 0, ll[7], 0)
                                self.list_match.append(mm.match)
                                mm.add_match(ll[6], 0, ll[5], 0)
                                self.list_match.append(mm.match)

            for row in self.list_match:
                p1 = row[0]
                p2 = row[1]

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

            valide = self.view.end_round()
            end_hour = ""
            if valide == "":
                end_hour = datetime.today().strftime('%H:%M')

            rr = rnd.Round("round " + str(num + 1), date, date_start, end_hour, self.list_match, )
            self.list_obj_round.append(jsons.dump(rr))
            # self.list_round = rr.matchs.copy()
            for row in rr.matchs:
                self.list_round.append(row)

        tr_object = tr.Tournament(idtournament, name, place, desc, time, 4, date, self.list_obj_round,
                                  self.list_player_json)
        print("classement")
        print(f" bis {self.ranking_bis}")

        # affichage classement
        liste_order = player.ranking_by_score(self.ranking_bis)
        val = player.check_same_score(liste_order)
        if val:
            liste_order = player.ranking_by_rank(liste_order)

        ll = player.return_list_object_from_dict(liste_order)

        for pla in ll:
            print(pla)

        tr_serialize = db.tournament_db(tr_object)
        db.add_tournament_db(tr_serialize)

        put = self.view.quit()
        if put == "":
            TournamentMenuController().__call__()

    # convertir en objet pour l'affichage
    def get_object_display(self):
        for i in self.players:
            player_obj = player.deserialize(i)
            self.players_obj.append(player_obj)

    # obtenir tous les participants
    def get_participant(self):
        for i in self.idplayer:
            json = db.get_player_by_id(i)
            play = player.deserialize(json)

            self.entrant.append(play)
            self.list_player_json.append(jsons.dump(play))


# lister tous les tournois
class DisplayTournamentController:

    def __init__(self):
        self.info = []
        liste = db.get_all_tournament()
        self.info = tr.Tournament.deserialize(liste)
        self.view = alltournamentview.AllTournamentView(self.info)

    def __call__(self):
        self.view.display_tournament()
        quit = self.view.quit()
        if quit == "":
            TournamentMenuController().__call__()


# Menu pour choisir trie liste de joueurs d"un tournoi
class MenuPlayerByTournamentController:

    def __init__(self):
        self.menu = menu
        self.view = menuplayerbytournamentview.MenuPlayerByTournamentView(self.menu)

    def __call__(self):
        self.menu.clear()
        self.menu.add("1", "Trier par ordre alphétique", PlayerByTournamentByNameController())
        self.menu.add("2", "Trier par classement", PlayerByTournamentByRankController())
        self.menu.add("3", "Retour", TournamentMenuController())

        user_choice = self.view.get_user_choice()
        check = self.menu.__contains__(user_choice)
        check = eval(check)

        while not check:
            self.view.display_error()
            user_choice = self.view.get_user_choice()
            check = self.menu.__contains__(user_choice)

        user_choice = self.view.return_controller(user_choice)
        user_choice.controller()


# Afficher les joueurs d'un tournoi par classement
class PlayerByTournamentByRankController:
    def __init__(self):

        self.info = []
        liste = db.get_all_tournament()
        self.info = tr.Tournament.deserialize(liste)
        self.list_obj = []
        self.view = playerbytournamentbyrankview.PlayerByTournamentByRank(self.info, self.list_obj)

    def __call__(self):

        self.view.display_tournament()
        val = self.view.get_user_choice()
        rs = db.get_all_player_by_tournament(val)
        for i in rs:
            pl = player.deserialize(i)
            self.list_obj.append(pl)
        self.list_obj.sort(key=lambda p: p.rank, reverse=False)
        self.view.display_player()
        quit = self.view.quit()
        if quit == "":
            MenuPlayerByTournamentController().__call__()


# Afficher les joueurs d'un tournoi par Nom
class PlayerByTournamentByNameController:
    def __init__(self):
        self.info = []
        liste = db.get_all_tournament()
        self.info = tr.Tournament.deserialize(liste)
        self.list_obj = []
        self.view = playerbytournamentbynameview.PlayerByTournamentByName(self.info, self.list_obj)

    def __call__(self):

        self.view.display_tournament()
        val = self.view.get_user_choice()
        rs = db.get_all_player_by_tournament(val)
        for i in rs:
            pl = player.deserialize(i)
            self.list_obj.append(pl)
        self.list_obj.sort(key=lambda p: p.lastname, reverse=False)
        self.view.display_player()
        quit = self.view.quit()
        if quit == "":
            MenuPlayerByTournamentController().__call__()


# Lister tous les matchs d'un tournoi
class MatchByTournament:

    def __init__(self):
        self.info = []
        liste = db.get_all_tournament()
        self.info = tr.Tournament.deserialize(liste)
        self.list_obj = []
        self.view = matchbytournamentview.MatchByTournament(self.info)

    def __call__(self):
        self.view.display_tournament()
        val = self.view.get_user_choice()
        liste = db.get_all_match_by_tournament(val)
        self.list_obj = match.Match.return_list_obj(self, liste)
        self.view.display_match(self.list_obj)
        put = self.view.quit()
        if put == "":
            TournamentMenuController().__call__()


# Liste de tous les tours d'un tournoi
class RoundByTournamentController:

    def __init__(self):
        self.info = []
        liste = db.get_all_tournament()
        self.info = tr.Tournament.deserialize(liste)
        self.list_obj = []
        self.view = roundbytournamentview.RoundByTournamentView(self.info)

    def __call__(self):
        self.view.display_tournament()
        val = self.view.get_user_choice()
        liste = db.get_all_match_by_tournament(val)
        self.list_obj = match.Match.return_list_obj(self, liste)
        dic = rnd.Round.return_dict_object(self.list_obj)
        self.view.display_round(dic)
        put =  self.view.quit()
        if put == "":
            TournamentMenuController().__call__()


