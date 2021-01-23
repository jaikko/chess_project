from tinydb import TinyDB, Query


# sérialisé player
def serialize_player(new):
    serialized_player = {
        'id': new.id,
        'firstname': new.first_name,
        'lastname': new.last_name,
        'date_of_birth': new.date_of_birth,
        'sexe': new.sexe,
        'rank': new.rank
    }
    return serialized_player


# ajouter player à la base de données
def add_db(serialized_players):
    db = TinyDB("player.json")
    players_table = db.table("players")
    players_table.insert(serialized_players)

#update tournament_players
def update_playerslist(liste, id):
    db = TinyDB("tournament.json")
    players_table = db.table("tournament")
    user = Query()
    result = players_table.search(user.id == id)
    result['players'] = liste
# ajouter tournaments à la base de données
def add_tournament_db(serialized_tr):
    db = TinyDB("tournament.json")
    players_table = db.table("tournament")
    players_table.insert(serialized_tr)


# récupérer le dernier idplayer et le retourner le nouvelle id
def get_id_player():
    db = TinyDB("player.json")
    players_table = db.table("players")
    num = len(players_table)
    if num >= 1:
        num += 1
    if num == 0:
        num = 1
    return num


# récupérer le dernier idtournament et le retourner le nouvelle id
def get_id_tournament():
    db = TinyDB("tournament.json")
    table = db.table("tournament")
    num = len(table)
    if num == 0:
        num = 1
    else:
        num += 1
    return num

#dbb tournoi
def tournament_db(tournament):
    serialized_tr = {
        'id': tournament.id,
        'players': tournament.players,
        'name': tournament.name,
        'place': tournament.place,
        'time': tournament.time,
        'laps': tournament.laps,
        'desc': tournament.desc
    }
    return serialized_tr



# récuper information à partir de l'id
def get_player_by_id(id):
    db = TinyDB("player.json")
    table = db.table("players")
    user = Query()
    result = table.search(user.id == int(id))
    return result


# récupérer tous les joueurs
def get_all_player():
    players = []
    db = TinyDB('player.json')
    table = db.table('players')
    for row in table:
        players.append(row)
    return players
