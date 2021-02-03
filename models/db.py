from tinydb import TinyDB, Query, where
from models import player, match


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


# récuper le dernier id
def get_max_id():
    db = TinyDB("data/player.json")
    num = len(db)
    return num


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


# récupérer tous les joueurs
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

    for n in range(4):
        for ke, ve in liste[n].items():
            if ke == "matchs":
                for i in ve:
                    liste_bis.append(i)

    return liste_bis
