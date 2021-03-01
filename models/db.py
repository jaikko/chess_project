import jsons
from tinydb import TinyDB, Query, where


# sérialisé player
def serialize_player(new):
    serialized_player = {
        'id': int(new.id),
        'firstname': new.firstname,
        'lastname': new.lastname,
        'date_of_birth': new.date_of_birth,
        'sexe': new.sexe,
        'rank': int(new.rank)
    }
    return serialized_player


# sérialisé round
def serialize_round(new):
    serialized_player = {
        'name': new.name,
        'date': new.date,
        'hour_end': new.hour_end,
        'hour_start': new.hour_start,
        'matchs': new.matchs
    }
    return serialized_player


# ajouter player à la base de données
def add_db(serialized_players):
    db = TinyDB("data/player.json")
    db.insert(serialized_players)


# update rank's player
def update_player_rank(id, rank):
    db = TinyDB("data/player.json")
    user = Query()
    db.update({'rank': int(rank)}, user.id == int(id))


# ajouter tournaments à la base de données
def add_tournament_db(serialized_tr):
    db = TinyDB("data/tournament.json")
    db.insert(serialized_tr)


# récupérer le dernier idplayer et le retourner le nouvelle id
def get_id_player():
    db = TinyDB("data/player.json")
    num = len(db)
    if num >= 1:
        num += 1
    if num == 0:
        num = 1
    return num


# récuper le dernier id player
def get_max_id():
    db = TinyDB("data/player.json")
    num = len(db)
    return num


# récuperer tous les id tournoi
def get_all_id_tr():
    db = TinyDB("data/tournament.json")
    liste = []
    for row in db:
        for k, v in row.items():
            if k == "id":
                liste.append(v)
    return liste


# récuperer tous les id joueur
def get_all_id_pl():
    db = TinyDB("data/player.json")
    liste = []
    for row in db:
        for k, v in row.items():
            if k == "id":
                liste.append(v)
    return liste


# récupérer le dernier idtournament et le retourner le nouvelle id
def get_id_tournament():
    db = TinyDB("data/tournament.json")
    num = len(db)
    if num == 0:
        num = 1
    else:
        num += 1
    return num


# dbb tournoi
def tournament_db(tournament):
    serialized_tr = {
        'id': tournament.id,
        'players': tournament.players,
        'name': tournament.name,
        'place': tournament.place,
        'time': tournament.time,
        'laps': tournament.laps,
        'desc': tournament.desc,
        'date': tournament.date,
        'round': tournament.round
    }
    return serialized_tr


# récuper information à partir de l'id
def get_player_by_id(id):
    db = TinyDB("data/player.json")
    user = Query()
    result = db.search(user.id == int(id))
    return result


# récupérer tous les joueurs
def get_all_player():
    players = []
    db = TinyDB('data/player.json')
    for row in db:
        players.append(row)
    return players


# récupérer tous les tournois
def get_all_tournament():
    liste = []
    db = TinyDB('data/tournament.json')
    for row in db:
        liste.append(row)
    return liste


# récupérer tous les joueurs d'un tournoi
def get_all_player_by_tournament(id):
    db = TinyDB('data/tournament.json')
    rs = db.search(where('id') == int(id))
    liste = []
    for k, v in rs[0].items():
        if k == "players":
            for i in v:
                liste.append(i)
    return liste


# récupérer tous les id des joueurs d'un tournoi
def get_all_player_id_by_tournament(id):
    db = TinyDB('data/tournament.json')
    rs = db.search(where('id') == int(id))
    liste = []
    for k, v in rs[0].items():
        if k == "players":
            for i in v:
                liste.append(i['id'])
    return liste


# récupérer nombre de round
def get_number_round(id):
    db = TinyDB('data/tournament.json')
    rs = db.search(where('id') == int(id))
    for k, v in rs[0].items():
        if k == "round":
            return len(v)


# récupérer  round
def get_round(id):
    db = TinyDB('data/tournament.json')
    rs = db.search(where('id') == int(id))
    for k, v in rs[0].items():
        if k == "round":
            return v


# récupérer tous les rounds d'un tournoi
def get_all_round_by_tournament(id):
    db = TinyDB('data/tournament.json')
    rs = db.search(where('id') == int(id))
    liste_bis = []

    for k, v in rs[0].items():
        if k == "round":
            for i in v:
                liste_bis.append(i)

    return liste_bis


# récupérer tous les matchs d'un tournoi
def get_all_match_by_tournament(id):
    db = TinyDB('data/tournament.json')
    rs = db.search(where('id') == int(id))
    liste = []
    liste_bis = []

    for k, v in rs[0].items():
        if k == "round":
            for i in v:
                liste.append(i)
    num = get_number_round(id)
    for n in range(num):
        for ke, ve in liste[n].items():
            if ke == "matchs":
                for i in ve:
                    liste_bis.append(i)
    return liste_bis


# update tournament round
def update_tr_round(id, r):
    old_liste = get_all_match_by_tournament(id)
    db = TinyDB("data/tournament.json")
    tr = Query()
    r_json = jsons.dump(r)

    if len(old_liste) < 4:

        db.update({'round': [r_json]}, tr.id == int(id))
    else:

        rv = get_round(id)

        if 4 <= len(old_liste) < 8:
            liste_json = [rv[0], r_json]
            db.update({'round': liste_json}, tr.id == int(id))
        if 8 <= len(old_liste) < 13:
            liste_json = [rv[0], rv[1], r_json]
            db.update({'round': liste_json}, tr.id == int(id))

        if 12 <= len(old_liste) < 16:
            liste_json = [rv[0], rv[1], rv[2], r_json]
            db.update({'round': liste_json}, tr.id == int(id))


# vérifier si rank identique

def same_rank():
    db = TinyDB('data/player.json')
    same = False
    players = []
    ranks = []

    for row in db:
        players.append(row)
    for r in db:
        ranks.append(r['rank'])

    for i in players:
        ranks.remove(i['rank'])
        if i['rank'] in ranks:
            same = True

    return same
