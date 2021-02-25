import json

from models import db


class Round:

    def __init__(self, name, date, hour_end, hour_start, matchs=[]):
        self.name = name
        self.date = date
        self.hour_end = hour_end
        self.hour_start = hour_start
        self.matchs = matchs

    @classmethod
    def deserialize(cls, json_string):
        liste = []
        for i in json_string:
            json_string = str(i).replace("\'", "\"").strip('[]')
            json_dict = json.loads(str(json_string))
            liste.append(cls(**json_dict))
        return liste


class RoundFunction:

    def __init__(self):
        pass

    @staticmethod
    def return_list_object(lm, id):

        len_match = len(db.get_all_match_by_tournament(id))
        list_tr = db.get_all_round_by_tournament(id)
        liste = Round.deserialize(list_tr)
        stock = []
        for count in range(1, len_match+1):

            if count < 5:
                if count == 4:
                    obj = liste[0]
                    rnd = Round(obj.name, obj.date, obj.hour_end, obj.hour_start, [lm[0], lm[1], lm[2], lm[3]])
                    stock.append(rnd)

            elif 4 < count < 9:
                if count == 8:
                    obj = liste[1]
                    rnd0 = Round(obj.name, obj.date, obj.hour_end, obj.hour_start, [lm[4], lm[5], lm[6], lm[7]])
                    stock.append(rnd0)

            elif 8 < count < 13:
                if count == 12:
                    obj = liste[2]
                    rnd1 = Round(obj.name, obj.date, obj.hour_end, obj.hour_start, [lm[8], lm[9], lm[10], lm[11]])
                    stock.append(rnd1)

            elif 12 < count < 17:
                if count == 16:
                    obj = liste[3]
                    rnd2 = Round(obj.name, obj.date, obj.hour_end, obj.hour_start, [lm[12], lm[13], lm[14], lm[15]])
                    stock.append(rnd2)

        return stock
