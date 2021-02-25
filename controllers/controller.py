import jsons as jsons
import sys

from datetime import datetime
from models import menu, player, db, tournament, match, round
from views.player import addplayer, editplayer, homemenu, playermenu, orderbyname, \
    orderbyrank
from views.tournament import newtournament, tournamentmenu, matchbytournament, playerbytournamentmenu, \
    playerbytournamentbyname, playerbytournamentbyrank, displayalltournament, roundbytournament

menu = menu.Menu()
players = player.Player
match_obj = match.Match
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
        self.view = homemenu.HomeMenuView(self.menu)

    def __call__(self):
        self.menu.clear()
        self.menu.add("1", "Gestion des joueurs", PlayerMenuController())
        self.menu.add("2", "Gestion des tournois", TournamentMenuController())
        self.menu.add("3", "Quitter", LeftController())
        user_choice = self.view.get_user_choice()
        check = self.menu.__contains__(user_choice)
        check = eval(check)

        while not check:
            self.view.display_error()
            user_choice = self.view.get_user_choice()
            check = self.menu.__contains__(user_choice)

        user_choice = self.view.return_controller(user_choice)
        user_choice.controller()


# Quiiter application
class LeftController:
    def __init__(self):
        pass

    def __call__(self):
        sys.exit()


# Menu Joueur
class PlayerMenuController:
    def __init__(self):
        self.menu = menu
        self.view = playermenu.PlayerMenuView(self.menu)

    def __call__(self):
        self.menu.clear()
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
        self.view = playermenu.PlayerMenuView(self.menu)

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
        self.players = players.return_list_object_from_list(self.players)
        self.players.sort(key=lambda p: p.lastname, reverse=False)

        self.view = orderbyname.PlayerOrderByNameView(self.players)

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
        self.players = players.return_list_object_from_list(self.players)
        self.players.sort(key=lambda p: p.rank, reverse=True)

        self.view = orderbyrank.PlayerOrderByNameView(self.players)

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
        self.view = addplayer.AddPlayerView(self.player)

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
        player_obj = player.Player(id, lastname, firstname, date_of_birth, sexe, rank)
        player_json = db.serialize_player(player_obj)
        db.add_db(player_json)
        put = self.view.quit()
        while put == "c":
            AddPlayerController().__call__()

        PlayerMenuController().__call__()


# Modifier rank d'un joueur
class EditPlayerController:
    def __init__(self):
        self.player = db.get_all_player()
        self.player = players.return_list_object_from_list(self.player)
        self.view = editplayer.EditPlayerView(self.player)

    def __call__(self):
        self.view.display_player()
        id = self.view.get_user_choice()
        all_id = db.get_all_id_pl()
        while not id.isdigit() or int(id) not in all_id:
            id = self.view.get_user_choice()
        json = db.get_player_by_id(id)
        p = players.deserialize(json)
        self.view.display_player_choice(p)
        rank = self.view.change_value()
        db.update_player_rank(id, rank)
        left = self.view.left()
        while left != "":
            left = self.view.left()
        PlayerMenuController().__call__()


# Menu Tournoi
class TournamentMenuController:
    def __init__(self):
        self.menu = menu
        self.view = tournamentmenu.TournamentMenuView(self.menu)

    def __call__(self):
        self.menu.clear()
        self.menu.add("1", "Créer un tournoi", NewTournamentController())
        self.menu.add("2", "Gérer un tournoi", ManageTournamentController())
        self.menu.add("3", "Liste de tous les tournois", DisplayTournamentController())
        self.menu.add("4", "Liste de tous les tours d'un tournoi", RoundByTournamentController())
        self.menu.add("5", "Liste de tous les matchs d'un tournoi", MatchByTournamentController())
        self.menu.add("6", "Liste de tous les joueurs d'un tournoi", PlayerByTournamentController())
        self.menu.add("7", "Retour", HomeMenuController())
        user_choice = self.view.get_user_choice()
        check = self.menu.__contains__(user_choice)
        check = eval(check)

        while not check:
            self.view.display_error()
            user_choice = self.view.get_user_choice()
            check = self.menu.__contains__(user_choice)

        user_choice = self.view.return_controller(user_choice)
        user_choice.controller()


# créer un nouveau tournoi
class NewTournamentController:
    def __init__(self):
        self.players = None
        self.time = tournament.Tournament.time
        self.players_obj = []
        self.view = newtournament.NewTournamentView(self.players_obj, self.time)
        self.count = 0
        self.idplayer = []
        self.entrant = []
        self.list_player_json = []
        self.list_round_json = []

    def __call__(self):
        self.players = db.get_all_player()
        self.get_object_display()
        maxi = db.get_max_id()
        list_date = []
        self.view.display_player()
        if db.same_rank():
            self.view.same_rank()
            PlayerMenuController().__call__()
        else:
            while self.count <= 7:

                choice = self.view.get_id_choice()

                while not choice.isdigit():
                    choice = self.view.get_id_choice()

                while int(choice) <= 0 or int(choice) > int(maxi):
                    self.view.error_id_availible()
                    choice = self.view.get_id_choice()

                while choice in self.idplayer:
                    self.view.error_id()
                    choice = self.view.get_id_choice()
                    while int(choice) > int(maxi):
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
                list_date.append(date)
                date = self.view.get_date()
                list_date.append(date)
                while not date:
                    date = self.view.get_date()
                put = self.view.check_date()
            self.view.show_time()
            time = self.view.get_time()
            while time not in ["bullet", "blitz", "coup rapide"]:
                time = self.view.get_time()
            desc = self.view.get_desc()

            self.get_participant()

            idtournament = db.get_id_tournament()
            if len(list_date) > 1:
                tr_object = tr.Tournament(idtournament, name, place, desc, time, 4, list_date, [],
                                          self.list_player_json)
            else:
                tr_object = tr.Tournament(idtournament, name, place, desc, time, 4, date, [], self.list_player_json)
            tr_serialize = db.tournament_db(tr_object)
            db.add_tournament_db(tr_serialize)

            put = self.view.quit()
            if put == "":
                TournamentMenuController().__call__()

    # convertir en objet pour l'affichage
    def get_object_display(self):
        for i in self.players:
            player_obj = players.deserialize(i)
            self.players_obj.append(player_obj)

    # obtenir tous les participants
    def get_participant(self):
        for i in self.idplayer:
            json = db.get_player_by_id(i)
            play = players.deserialize(json)

            self.entrant.append(play)
            self.list_player_json.append(jsons.dump(play))


# Gérer un tournoi
class ManageTournamentController:

    def __init__(self):
        self.info = []
        liste = db.get_all_tournament()
        self.info = tr.Tournament.deserialize(liste)
        self.view = matchbytournament.MatchByTournament(self.info)
        self.list_match = []
        self.ranking_bis = {}
        self.list_round = []
        self.ranking = {}
        self.round_str = []
        self.final_rank = []

    def __call__(self):
        num = 0
        self.view.display_tournament()
        put = self.view.get_user_choice()
        all_tr = db.get_all_id_tr()
        while not put.isdigit() or int(put) not in all_tr:
            put = self.view.get_user_choice()

        # récuper nombre du dernier round
        num_round = db.get_number_round(put)

        # récuper tous les joueurs du tournoi
        all_player = db.get_all_player_by_tournament(put)
        all_player = players.return_list_object_from_list(all_player)

        for count in range(4 - num_round):
            self.list_match.clear()
            # récuperer nombre de round
            num_round = db.get_number_round(put)
            # génération de la date
            date = datetime.today().strftime('%d-%m-%Y')
            # génération de l'heure de début
            date_start = datetime.today().strftime('%H:%M')

            if num_round == 0:

                num += 1
                liste_a, liste_b = player.PlayerFunction.split_player_by_rank(all_player)
                for h in range(4):
                    m = match_obj(liste_a[h], 0, liste_b[h], 0)

                    self.list_match.append(m.match)

            if 1 <= num_round < 4:
                if num == 0:
                    num += num_round + 1
                else:
                    num = num_round + 1
                # print(self.ranking_bis)
                if len(self.ranking_bis) < 8:
                    self.ranking_bis = player.PlayerFunction.get_score_by_player(put)
                liste_order = player.PlayerFunction.ranking_by_score(self.ranking_bis)
                # print(liste_order)
                val = player.PlayerFunction.check_same_score(liste_order)
                if val:
                    liste_order = player.PlayerFunction.ranking_by_rank(liste_order)
                    # print(liste_order)

                    new_liste = players.return_list_object_from_dict(liste_order)
                    for j in range(0, 7, 2):
                        m = match.Match(new_liste[j], 0, new_liste[j + 1], 0)
                        self.list_match.append(m.match)
                    new_liste.clear()

                    # vérification des matchs
                    all_match = self.list_match.copy()
                    self.list_match = match.MatchFunction.check_match2(put, self.list_match)
                    if len(self.list_match) == 0:
                        self.list_match = all_match.copy()

            # afficher match
            for row in self.list_match:
                self.view.display_new_match(row)
                winner = self.view.get_winner()
                while winner not in ['1', '2', ""]:
                    winner = input("gagnant(numéro du joueur) si match nul appuyez sur entrée: ")
                if winner == "1":
                    row[0][1] += 1
                elif winner == "2":
                    row[1][1] += 1
                elif not winner:
                    row[0][1] += 0.5
                    row[1][1] += 0.5

            valide = self.view.end_round()
            while valide != "":
                valide = self.view.end_round()
            end_hour = datetime.today().strftime('%H:%M')

            rr = rnd.Round("round " + str(num), date, date_start, end_hour, self.list_match)
            db.update_tr_round(put, rr)

            if num_round <= 3:
                if num_round == 3:
                    # générer classement
                    self.ranking_bis = player.PlayerFunction.get_score_by_player(put)
                    self.final_rank = player.PlayerFunction.ranking_by_score(self.ranking_bis)
                    val = player.PlayerFunction.check_same_score(self.final_rank)
                    if val:
                        self.final_rank = player.PlayerFunction.ranking_by_rank(self.final_rank)
                    pla = players.return_list_object_from_dict(self.final_rank)
                    self.view.display_rank_final(pla)

                    # modifier classement joueur
                    edit = self.view.choice_edit_player()
                    while edit not in ["", "o"]:
                        edit = self.view.choice_edit_player()

                    if edit == "":
                        TournamentMenuController().__call__()
                    while edit == "o":
                        all_pl = db.get_all_player_by_tournament(put)
                        all_pl_obj = []
                        for i in all_pl:
                            player_obj = players.deserialize(i)
                            all_pl_obj.append(player_obj)

                        self.view.display_player(all_pl_obj)
                        all_id = db.get_all_player_id_by_tournament(put)
                        enter_id = self.view.edit_player_id()
                        while not enter_id.isdigit() or int(enter_id) not in all_id:
                            enter_id = self.view.edit_player_id()

                        rank = self.view.change_value()
                        while not rank.isdigit():
                            rank = self.view.change_value()
                        db.update_player_rank(enter_id, rank)
                        left = self.view.left_edit()
                        while left not in ["", "o"]:
                            left = self.view.left_edit()

                        # quitter tournoi à la fin
                        if left == "":
                            edit = ""
                            TournamentMenuController().__call__()

                else:
                    enter = self.view.left()
                    while enter not in ["", "o"]:
                        enter = self.view.left()
                    if enter == "":
                        TournamentMenuController().__call__()
                    elif enter == "o":
                        for i in self.list_match:
                            self.ranking[i[0][0].id] = i[0][1]
                            self.ranking[i[1][0].id] = i[1][1]

            if num_round == 0:
                self.ranking_bis = self.ranking.copy()
                # print(self.ranking_bis)
                count += 1
            else:
                count += 1
                for k, v in self.ranking.items():
                    for key, val in self.ranking_bis.items():

                        if k == key:
                            value = val + v

                            self.ranking_bis[k] = value

        if num_round > 3:
            # générer classement
            self.ranking_bis = player.PlayerFunction.get_score_by_player(put)
            self.final_rank = player.PlayerFunction.ranking_by_score(self.ranking_bis)
            val = player.PlayerFunction.check_same_score(self.final_rank)
            if val:
                self.final_rank = player.PlayerFunction.ranking_by_rank(self.final_rank)
            pla = players.return_list_object_from_dict(self.final_rank)
            self.view.display_rank_final(pla)

            left = self.view.quit()
            while left not in ["", "o"]:
                left = self.view.quit()

            # quitter tournoi à la fin
            if left == "":
                TournamentMenuController().__call__()


# Lister tous les matchs d'un tournoi
class MatchByTournamentController:

    def __init__(self):
        self.info = []
        liste = db.get_all_tournament()
        self.info = tr.Tournament.deserialize(liste)
        self.list_obj = []
        self.view = matchbytournament.MatchByTournament(self.info)

    def __call__(self):
        self.view.display_tournament()
        val = self.view.get_user_choice()
        all_tr = db.get_all_id_tr()
        while not val.isdigit() or int(val) not in all_tr:
            val = self.view.get_user_choice()
        liste2 = db.get_all_match_by_tournament(val)
        self.list_obj = match.MatchFunction.return_list_obj(liste2)
        self.view.display_match(self.list_obj)
        put = self.view.quit()
        if put == "":
            TournamentMenuController().__call__()


# Menu pour choisir tri liste de joueurs d'un tournoi
class PlayerByTournamentController:

    def __init__(self):
        self.menu = menu
        self.view = playerbytournamentmenu.PlayerByTournament(self.menu)

    def __call__(self):
        self.menu.clear()
        self.menu.add("1", "Trier par ordre alphétique", PlayerByTournamentByNameController())
        self.menu.add("2", "Trier par classement", PlayerByTournamentByRankController())
        self.menu.add("3", "Retour", TournamentMenuController())

        user_choice = self.view.get_user_choice()
        check = self.menu.__contains__(user_choice)
        check = eval(check)

        while not check:
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
        self.view = playerbytournamentbyrank.PlayerByTournamentByRank(self.info, self.list_obj)

    def __call__(self):

        self.view.display_tournament()
        val = self.view.get_user_choice()
        all_tr = db.get_all_id_tr()
        while not val.isdigit() or int(val) not in all_tr:
            val = self.view.get_user_choice()
        rs = db.get_all_player_by_tournament(val)
        for i in rs:
            pl = players.deserialize(i)
            self.list_obj.append(pl)
        self.list_obj.sort(key=lambda p: p.rank, reverse=True)
        self.view.display_player()
        quit = self.view.quit()
        while quit != "":
            quit = self.view.quit()
        PlayerByTournamentController().__call__()


# Afficher les joueurs d'un tournoi par Nom
class PlayerByTournamentByNameController:
    def __init__(self):
        self.info = []
        liste = db.get_all_tournament()
        self.info = tr.Tournament.deserialize(liste)
        self.list_obj = []
        self.view = playerbytournamentbyname.PlayerByTournamentByName(self.info, self.list_obj)

    def __call__(self):

        self.view.display_tournament()
        val = self.view.get_user_choice()
        all_tr = db.get_all_id_tr()
        while not val.isdigit() or int(val) not in all_tr:
            val = self.view.get_user_choice()
        rs = db.get_all_player_by_tournament(val)
        for i in rs:
            pl = players.deserialize(i)
            self.list_obj.append(pl)
        self.list_obj.sort(key=lambda p: p.lastname, reverse=False)
        self.view.display_player()
        quit = self.view.quit()
        while quit != "":
            quit = self.view.quit()
        PlayerByTournamentController().__call__()


# Afficher la liste des tournois
class DisplayTournamentController:

    def __init__(self):
        self.info = []
        liste = db.get_all_tournament()
        self.info = tr.Tournament.deserialize(liste)
        self.view = displayalltournament.DisplayAllTournament(self.info)

    def __call__(self):
        self.view.display_tournament()
        quit = self.view.quit()
        while quit != "":
            quit = self.view.quit()
        TournamentMenuController().__call__()


# Afficher la liste des rounds d'un tournoi
class RoundByTournamentController:

    def __init__(self):
        self.info = []
        liste = db.get_all_tournament()
        self.info = tr.Tournament.deserialize(liste)
        self.list_obj = []
        self.view = roundbytournament.RoundByTournamentView(self.info)

    def __call__(self):
        self.view.display_tournament()
        val = self.view.get_user_choice()
        all_tr = db.get_all_id_tr()
        while not val.isdigit() or int(val) not in all_tr:
            val = self.view.get_user_choice()
        liste = db.get_all_match_by_tournament(val)
        self.list_obj = match.MatchFunction.return_list_obj(liste)
        my_list = rnd.RoundFunction.return_list_object(self.list_obj, val)
        self.view.display_round(my_list)
        put = self.view.quit()
        if put == "":
            TournamentMenuController().__call__()
