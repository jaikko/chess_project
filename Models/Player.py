from tinydb import TinyDB, Query


class Player:
    list_player = []

    def __init__(self, id, first_name, last_name, date_of_birth, sexe, rank):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.sexe = sexe
        self.rank = rank



def show_player():
    db = TinyDB('db.json')
    table = db.table('players')


    for row in table:
        print(row['idd'] + ":" + " Prénom:" + row['firstname'] + " ,Nom:" + row['lastname']
              + " ,date de naissance:" + row['date_of_birth'] + " ,Sexe:" + row['sexe'] + " ,Rang:" + row['rank'])

