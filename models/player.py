import json
import operator
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

    def __eq__(self, other):
        return self.rank == other.rank

    def __lt__(self, other):
        return self.rank < other.rank

    @classmethod
    def deserialize(cls, json_string):
        json_string = str(json_string).replace("\'", "\"").strip('[]')
        json_dict = json.loads(str(json_string))
        return cls(**json_dict)

    @staticmethod
    def split_player(liste):
        liste.sort(key=lambda p: p.rank, reverse=True)
        liste_a = liste[0:4]
        liste_b = liste[4:8]

        return liste_a, liste_b

    @staticmethod
    def ranking_by_rank(self, liste):
        all = []
        old_id = ""
        old_value = ""
        count = 0
        d2 = ""
        list_same = []
        dd = {}
        for k, v in liste.items():
            count += 1
            if k not in list_same:
                if old_value == v:
                    list_same.append(k)
                    list_same.append(old_id)
                    if count == 8:
                        for i in list_same:
                            json = db.get_player_by_id(i)
                            obj = self.deserialize(json)
                            dd[obj.rank] = obj.id
                            d2 = OrderedDict(sorted(dd.items(), key=lambda t: t[0], reverse=True))

                        for ke, va in d2.items():
                            all.append(va)
                        d2.clear()
                        dd.clear()
                        list_same.clear()
                if old_value != v:

                    if len(list_same) > 1:
                        for i in list_same:
                            json = db.get_player_by_id(i)
                            obj = self.deserialize(json)
                            dd[obj.rank] = obj.id
                            d2 = OrderedDict(sorted(dd.items(), key=lambda t: t[0], reverse=True))

                        for ke, va in d2.items():
                            all.append(va)
                        d2.clear()
                        dd.clear()
                        list_same.clear()
            old_id = k
            old_value = v
        print(all)
        return all

    @staticmethod
    def ranking_by_score(liste):
        liste_ordered = {}
        for k, v in sorted(liste.items(), key=lambda x: x[1], reverse=True):
            liste_ordered[k] = v
        return liste_ordered


class Test:

    def __init__(self, rank):
        self.rank = rank
