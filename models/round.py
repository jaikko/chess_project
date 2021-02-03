class Round:

    def __init__(self, name, date, hour_end, hour_start, matchs=[]):
        self.name = name
        self.date = date
        self.hour_end = hour_end
        self.hour_start = hour_start
        self.matchs = matchs

    @staticmethod
    def return_dict_object(liste_matchs):

        count = 0
        new_liste = []
        dic = {}
        last_dic = {}
        stock = []

        for i in liste_matchs:
            count += 1
            if count < 5:
                new_liste.append(i)
                if count == 4:
                    dic['Round 1'] = new_liste

            elif 4 < count < 9:
                new_liste.append(i)
                if count == 8:
                    dic['Round 2'] = new_liste
                    new_liste.clear()
            elif 8 < count < 13:
                new_liste.append(i)
                if count == 12:
                    dic['Round 3'] = new_liste
                    new_liste.clear()

            elif 12 < count < 17:
                new_liste.append(i)
                if count == 16:
                    dic['Round 4'] = new_liste
                    return dic








