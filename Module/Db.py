from tinydb import TinyDB, Query


# sérialisé player
def serialize_player(new_player):
    serialized_player = {
        'id': new_player.id,
        'firstname': new_player.first_name,
        'lastname': new_player.last_name,
        'date_of_birth': new_player.date_of_birth,
        'sexe': new_player.sexe,
        'rank': new_player.rank
    }
    return serialized_player

# désérialiser player

def unserialize_player(json, player):
    pass


# ajouter player à la base de données
def add_db(serialized_players):
    db = TinyDB("db.json")
    players_table = db.table("players")
    # players_table.truncate()  # clear the table first
    players_table.insert(serialized_players)


# récupérer le dernier id et le retourner le nouvelle id
def get_id_player():
    db = TinyDB("db.json")
    players_table = db.table("players")
    num = len(players_table)
    if num == 1:
        num += 1
    elif num == 0:
        num = 1
    return num


# afficher les joueurs
def show_player():
    db = TinyDB('db.json')
    table = db.table('players')

    for row in table:
        print("id:" + str(row['id'] )+ ":" + " Prénom:" + row['firstname'] + " ,Nom:" + row['lastname']
              + " ,date de naissance:" + row['date_of_birth'] + " ,Sexe:" + row['sexe'] + " ,Rang:" + row['rank'])

# ajouter joueur à la table playerbytournament
def player_by_tournament(idtournament, idplayer):
    serial = {
        'idtournament' : idtournament,
        'idplayer' : idplayer
    }
    db = TinyDB("db.json")
    table = db.table("playerbytournement")
    table.insert(serial)

def get_player_by_id(id):
    db = TinyDB("db.json")
    table = db.table("players")
    user = Query()
    return table.search(user.id == id)



