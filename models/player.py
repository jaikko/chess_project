import json
from collections import OrderedDict

from models import db


class Player:

    def __init__(self, id, firstname, lastname, date_of_birth, sexe, rank):
        self.id = id
        self.first_name = firstname
        self.last_name = lastname
        self.date_of_birth = date_of_birth
        self.sexe = sexe
        self.rank = rank

    def __str__(self):
        return f" id: {self.id} nom: {self.last_name} prenom: {self.first_name} date de naissance: {self.date_of_birth}" \
               f" sexe: {self.sexe}  rank {self.rank}"

    @classmethod
    def deserialize(cls, json_string):
        json_string = str(json_string).replace("\'", "\"").strip('[]')
        json_dict = json.loads(str(json_string))
        return cls(**json_dict)

    @staticmethod
    def split_player_by_rank(liste):
        liste.sort(key=lambda p: p.rank, reverse=True)
        liste_a = liste[0:4]
        liste_b = liste[4:8]

        return liste_a, liste_b

    @staticmethod
    def split_player_by_score(liste):
        list_obj = []
        for k, v in liste.items():
            json = db.get_player_by_id(k)
            play = Player.deserialize(json)
            list_obj.append(play)
        liste_a = list_obj[0:4]
        liste_b = list_obj[4:8]

        return liste_a, liste_b

    @staticmethod
    def ranking_by_rank(liste):
        all = []
        old_id = ""
        old_value = ""
        count = 0
        d2 = ""
        list_same = []
        dd = {}
        enter = False
        for k, v in liste.items():
            count += 1
            if k not in list_same:
                if old_value == v:
                    list_same.append(k)
                    list_same.append(old_id)
                    if count == 8:
                        for i in list_same:
                            json = db.get_player_by_id(i)
                            obj = Player.deserialize(json)
                            dd[obj.rank] = obj.id
                            d2 = OrderedDict(sorted(dd.items(), key=lambda t: t[0], reverse=True))

                        for ke, va in d2.items():
                            all.append(va)
                        d2.clear()
                        dd.clear()
                        list_same.clear()
                if old_value != v:

                    if len(list_same) > 1:
                        enter += True
                        for i in list_same:
                            json = db.get_player_by_id(i)
                            obj = Player.deserialize(json)
                            dd[obj.rank] = obj.id
                            d2 = OrderedDict(sorted(dd.items(), key=lambda t: t[0], reverse=True))

                        for ke, va in d2.items():
                            all.append(va)
                        d2.clear()
                        dd.clear()
                        list_same.clear()

                    if len(list_same) == 0 and old_id != "":
                        if count == 8:
                            all.append(old_id)
                            all.append(k)

                        if count != 8 and not enter:
                            all.append(old_id)

            old_id = k
            old_value = v

        score = ""
        dictio = {}
        for i in all:
            for k, v in liste.items():
                if k == i:
                    score = v

                dictio[k] = v

        return dictio

    @staticmethod
    def ranking_by_score(liste):
        liste_ordered = {}
        for k, v in sorted(liste.items(), key=lambda x: x[1], reverse=True):
            liste_ordered[k] = v
        return liste_ordered

    @staticmethod
    def check_same_score(liste):
        old_score = ""
        check = False
        for v in liste.values():
            if v == old_score:
                check += True

            old_score = v

        return check

    @classmethod
    def return_list_object_from_dict(cls, liste):
        list_obj = []
        for k, v in liste.items():
            json = db.get_player_by_id(k)
            play = Player.deserialize(json)
            list_obj.append(play)
        return list_obj

    @classmethod
    def return_list_object_from_list(cls, liste):
        list_obj = []
        for i in liste:
            play = Player.deserialize(i)
            list_obj.append(play)
        return list_obj



