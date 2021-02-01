from tinydb import TinyDB, Query


# sérialisé player
def serialize_player(new):
    serialized_player = {
        'id': int(new.id),
        'firstname': new.first_name,
        'lastname': new.last_name,
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
