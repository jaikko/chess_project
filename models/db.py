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
    db = TinyDB("db.json")
    players_table = db.table("players")
    # players_table.truncate()  # clear the table first
    players_table.insert(serialized_players)


# récupérer le dernier idplayer et le retourner le nouvelle id
def get_id_player():
    db = TinyDB("db.json")
    players_table = db.table("players")
    num = len(players_table)
    if num >= 1:
        num += 1
    if num == 0:
        num = 1
    return num


# récupérer le dernier idtournament et le retourner le nouvelle id
def get_id_tournament():
    db = TinyDB("db.json")
    table = db.table("playerbytournement")
    num = len(table)
    if num == 0:
        num = 0
    else:
        num = int(num/2)
    return num


# ajouter joueur à la table playerbytournament
def player_by_tournament(idtournament, idplayer):
    serial = {
        'idtournament': idtournament,
        'idplayer': idplayer
    }
    db = TinyDB("db.json")
    table = db.table("playerbytournement")
    table.insert(serial)


# récuper information à partir de l'id
def get_player_by_id(id):
    db = TinyDB("db.json")
    table = db.table("players")
    user = Query()
    result = table.search(user.id == id)
    return result


# vérifier joueur inscrit à un tournoi
def check_idplayer_tournament(idtournament, idplayer):
    idtournament = int(idtournament)
    idplayer = int(idplayer)
    db = TinyDB("db.json")
    table = db.table("playerbytournement")
    user = Query()
    result = table.search((user.idtournament == idtournament) & (user.idplayer == idplayer))
    return len(result)


# récupérer tous les joueurs
def get_all_player():
    players = []
    db = TinyDB('db.json')
    table = db.table('players')
    for row in table:
        players.append(row)
    return players
