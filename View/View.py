from Models import models
from Module import Db


def add_player(id):
    finish = False
    while not finish:
        first_name = input("first_name")
        last_name = input("last_name")
        date_of_birth = input("date of birth")
        sexe = input("sexe")
        rank = input("rank")

        value = input("Pour ajouter un nouveau joueur, appuyer sur o sinon appuyez sur q pour quitter")
        if value == "q":
            finish = False

        return models.Player(id, first_name, last_name, date_of_birth, sexe, rank)


def add_tournament():
    name = input("nom")
    place = input("lieu")
    date = input("date")

    player = []

    count = 0
    while count <= 7:
        print("ajouter joueur au tournoi")
        Db.show_player()
        id = input("entrez l'id du joueur à ajouter: ")
        Db.player_by_tournament(1, id)
        info = Db.get_player_by_id(id)
        player.append(info)
        count += 1
