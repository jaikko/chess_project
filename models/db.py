from tinydb import TinyDB, Query


class Db:
    def __init__(self):
        pass

    # sérialisé player
    def serialize_player(self, new):
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
    def add_db(self, serialized_players):
        db = TinyDB("db.json")
        players_table = db.table("players")
        # players_table.truncate()  # clear the table first
        players_table.insert(serialized_players)

    # récupérer le dernier idplayer et le retourner le nouvelle id
    def get_id_player(self):
        db = TinyDB("db.json")
        players_table = db.table("players")
        num = len(players_table)
        print("num" + str(num))
        if num >= 1:
            num += 1
        if num == 0:
            num = 1
        return num

    # récupérer le dernier idtournament et le retourner le nouvelle id
    def get_id_tournament(self):
        db = TinyDB("db.json")
        table = db.table("playerbytournement")
        num = len(table)
        if num >= 1:
            num += 1
        elif num == 0:
            num = 1
        return num

    # afficher les joueurs

    def show_player(self):
        db = TinyDB('db.json')
        table = db.table('players')

        for row in table:
            print("id:" + str(row['id']) + "," + " Prénom:" + row['firstname'] + " ,Nom:" + row['lastname']
                  + " ,date de naissance:" + row['date_of_birth'] + " ,Sexe:" + row['sexe'] + " ,Rang:" + row[
                      'rank'])

    # ajouter joueur à la table playerbytournament
    def player_by_tournament(self,idtournament, idplayer):
        serial = {
            'idtournament': idtournament,
            'idplayer': idplayer
        }
        db = TinyDB("db.json")
        table = db.table("playerbytournement")
        table.insert(serial)

    def get_player_by_id(self, id):

        db = TinyDB("db.json")
        table = db.table("players")
        user = Query()
        result = table.search(user.id == id)
        return result
