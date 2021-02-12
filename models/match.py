import random

from models import player, db, round


class Match:
    match = ()

    def __init__(self, p1, s1, p2, s2):
        self.p1 = p1
        self.p2 = p2
        self.s1 = s1
        self.s2 = s2
        self.match = ([p1, s1], [p2, s2])

    # def __str__(self):
    # return print(f" {self.p1.lastname} vs {self.p2.lastname}")

    def get_match(self):
        return print(f" {self.p1} vs {self.p2}")

    def items(self):
        return self.match.items()

    def return_match(self):
        return f"Joueur 1: {self.match[0].player.first_name} "

    # def check_match(id, list_object):
    #
    #     print("check")
    #     cc = 0
    #     list_match = db.get_all_match_by_tournament(id)
    #     list_match =
    #     print(list_match)
    #
    #     print(list_match)
    #
    #     new_match = []
    #
    #     for ad in list_object:
    #
    #         cc += 1
    #         pl1 = ad[0][0].id
    #         pl2 = ad[1][0].id
    #
    #         for row in list_match:
    #
    #
    #             if row[0][0].id == pl1 and row[1][0].id == pl2 or row[0][0].id == pl2 \
    #                     and row[1][0].id == pl1:
    #
    #                 if cc in [1, 5, 9]:
    #
    #                     print("error")
    #                     new_match.clear()
    #                     m1 = Match(list_object[0], 0, list_object[2], 0)
    #                     new_match.append(m1.match)
    #                     m2 = Match(list_object[1], 0, list_object[3], 0)
    #                     new_match.append(m2.match)
    #                     m3 = Match(list_object[4], 0, list_object[5], 0)
    #                     new_match.append(m3.match)
    #                     m4 = Match(list_object[6], 0, list_object[7], 0)
    #                     new_match.append(m4.match)
    #
    #                     error = False
    #
    #                     for a in list_object:
    #
    #                         pl1 = a[0].player.id
    #                         pl2 = a[1].player.id
    #                         for rows in new_match:
    #                             if rows[0][0].id == pl1 and rows[1][0].id == pl2 or rows[1][0].id == pl2 \
    #                                     and rows[1][0].id == pl1:
    #                                 error += True
    #
    #                     while error:
    #                         liste = [0, 1, 2]
    #                         num = 3
    #                         liste.append(num)
    #                         list_match.clear()
    #                         m = Match(list_object[0], 0, list_object[num], 0)
    #                         list_match.append(m)
    #                         r = random.randint(3, 8)
    #                         while r in liste:
    #                             r = random.randint(3, 8)
    #                         liste.append(r)
    #                         m = Match(list_object[1], 0, list_object[r], 0)
    #                         list_match.append(m)
    #                         r2 = random.randint(3, 8)
    #                         while r in liste:
    #                             r2 = random.randint(3, 8)
    #                         liste.append(r2)
    #                         m = Match(list_object[2], 0, list_object[r2], 0)
    #                         list_match.append(m)
    #                         r3 = 0
    #                         for i in range(3, 8):
    #                             if i not in liste:
    #                                 r3 += i
    #                                 liste.append(i)
    #                         r4 = 0
    #                         for i in range(3, 8):
    #                             if i not in liste:
    #                                 r4 += i
    #                                 liste.append(i)
    #                         m = Match(list_object[r3], 0, list_object[r4], 0)
    #                         list_match.append(m)
    #                         num += 1
    #                         for a in list_object:
    #
    #                             pl1 = a[0].player.id
    #                             pl2 = a[1].player.id
    #                             for rows in list_match:
    #                                 if rows.p1.id != pl1 and rows.p2.id != pl2 or rows.p1.id != pl2 \
    #                                         and rows.p2.id != pl1:
    #                                     error += False
    #
    #                 # if cc in [2, 6, 10]:
    #                 #
    #                 #     error = True
    #                 #
    #                 #     while error:
    #                 #         liste = [0, 1, 2, 3]
    #                 #         list_match.clear()
    #                 #         m = Match(list_object[0], 0, list_object[1], 0)
    #                 #         list_match.append(m)
    #                 #         r = random.randint(2, 7)
    #                 #         while r in liste:
    #                 #             r = random.randint(4, 8)
    #                 #         liste.append(r)
    #                 #         m = Match(list_object[2], 0, list_object[r], 0)
    #                 #         list_match.append(m)
    #                 #         r2 = random.randint(4, 8)
    #                 #         while r in liste:
    #                 #             r2 = random.randint(1, 7)
    #                 #         liste.append(r2)
    #                 #         m = Match(list_object[3], 0, list_object[r2], 0)
    #                 #         list_match.append(m)
    #                 #         r3 = 0
    #                 #         for i in range(4, 8):
    #                 #             if i not in liste:
    #                 #                 r3 += i
    #                 #                 liste.append(i)
    #                 #         r4 = 0
    #                 #         for i in range(4, 8):
    #                 #             if i not in liste:
    #                 #                 r4 += i
    #                 #                 liste.append(i)
    #                 #         m = Match(list_object[r3], 0, list_object[r4], 0)
    #                 #         list_match.append(m)
    #                 #
    #                 #         for a in list_round:
    #                 #
    #                 #             pl1 = a[0].player.id
    #                 #             pl2 = a[1].player.id
    #                 #             for rows in list_match:
    #                 #
    #                 #                 if rows.p1.id != pl1 and rows.p2.id != pl2 or rows.p1.id != pl2 \
    #                 #                         and rows.p2.id != pl1:
    #                 #                     error += False
    #                 #
    #                 # if cc in [3, 7, 11]:
    #                 #
    #                 #     error = True
    #                 #
    #                 #     while error:
    #                 #         liste = [0, 1, 4, 5]
    #                 #         list_match.clear()
    #                 #         m = Match(list_object[0], 0, list_object[1], 0)
    #                 #         list_match.append(m)
    #                 #         r = random.randint(2, 8)
    #                 #         while r in liste:
    #                 #             r = random.randint(1, 7)
    #                 #         liste.append(r)
    #                 #         m = Match(list_object[4], 0, list_object[r], 0)
    #                 #         list_match.append(m)
    #                 #         r2 = random.randint(2, 8)
    #                 #         while r in liste:
    #                 #             r2 = random.randint(2, 8)
    #                 #         liste.append(r2)
    #                 #         m = Match(list_object[5], 0, list_object[r2], 0)
    #                 #         list_match.append(m)
    #                 #         r3 = 0
    #                 #         for i in range(2, 8):
    #                 #             if i not in liste:
    #                 #                 r3 += i
    #                 #                 liste.append(i)
    #                 #         r4 = 0
    #                 #         for i in range(2, 8):
    #                 #             if i not in liste:
    #                 #                 r4 += i
    #                 #                 liste.append(i)
    #                 #         m = Match(list_object[r3], 0, list_object[r4], 0)
    #                 #         list_match.append(m)
    #                 #
    #                 #         for a in list_round:
    #                 #
    #                 #             pl1 = a[0].player.id
    #                 #             pl2 = a[1].player.id
    #                 #             for rows in list_match:
    #                 #                 if rows.p1.id != pl1 and rows.p2.id != pl2 or rows.p1.id != pl2 \
    #                 #                         and rows.p2.id != pl1:
    #                 #                     error += False
    #                 #
    #                 # if cc in [4, 8, 12]:
    #                 #
    #                 #     error = True
    #                 #
    #                 #     while error:
    #                 #         liste = [0, 1, 6, 7]
    #                 #         list_match.clear()
    #                 #         m = Match(list_object[0], 0, list_object[1], 0)
    #                 #         list_match.append(m)
    #                 #         r = random.randint(2, 6)
    #                 #         while r in liste:
    #                 #             r = random.randint(2, 6)
    #                 #         liste.append(r)
    #                 #         m = Match(list_object[5], 0, list_object[r], 0)
    #                 #         list_match.append(m)
    #                 #         r2 = random.randint(2, 6)
    #                 #         while r in liste:
    #                 #             r2 = random.randint(2, 6)
    #                 #         liste.append(r2)
    #                 #         m = Match(list_object[6], 0, list_object[r2], 0)
    #                 #         list_match.append(m)
    #                 #         r3 = 0
    #                 #         for i in range(2, 6):
    #                 #             if i not in liste:
    #                 #                 r3 += i
    #                 #                 liste.append(i)
    #                 #         r4 = 0
    #                 #         for i in range(2, 6):
    #                 #             if i not in liste:
    #                 #                 r4 += i
    #                 #                 liste.append(i)
    #                 #         m = Match(list_object[r3], 0, list_object[r4], 0)
    #                 #         list_match.append(m)
    #                 #
    #                 #         for a in list_round:
    #                 #
    #                 #             p1 = a[0].player.id
    #                 #             p2 = a[1].player.id
    #                 #             for rows in list_match:
    #                 #                 if rows[0].player.id != p1 and rows[1].player.id != p2 or rows[
    #                 #                     0].player.id != p2 \
    #                 #                         and rows[1].player.id != p1:
    #                 #                     error += False
    #     return list_object

    @staticmethod
    def return_list_obj(liste):
        pl1 = ""
        pl2 = ""
        score1 = ""
        score2 = ""
        count = 0
        liste_obj = []
        for g in liste:
            pl1 = player.Player.deserialize(g[0][0])
            score1 = g[0][1]
            pl2 = player.Player.deserialize(g[1][0])
            score2 = g[1][1]

            m = Match(pl1, score1, pl2, score2)
            liste_obj.append(m)
        return liste_obj


class MatchFunction:

    def __init__(self):
        pass

    @staticmethod
    def check_match(id, list_object):

        print("check")
        cc = 0
        list_match = db.get_all_match_by_tournament(id)
        list_match = Match.return_list_obj(list_match)
        new_match = []
        error = False
        for ad in list_object:

            cc += 1
            pl1 = ad[0][0].id
            pl2 = ad[1][0].id

            for row in list_match:
                if row.p1.id == pl1 and row.p2.id == pl2 or row.p1.id == pl2 and row.p2.id == pl1:

                    print(cc)
                    if cc in [1, 5, 9]:

                        print("error")
                        new_match.clear()
                        m1 = Match(list_object[0][0][0], 0, list_object[1][0][0], 0)
                        new_match.append(m1.match)
                        m2 = Match(list_object[0][1][0], 0, list_object[1][1][0], 0)
                        new_match.append(m2.match)
                        m3 = Match(list_object[2][0][0], 0, list_object[2][1][0], 0)
                        new_match.append(m3.match)
                        m4 = Match(list_object[3][0][0], 0, list_object[3][1][0], 0)
                        new_match.append(m4.match)

                        for a in new_match:

                            pl1 = a[0][0].id
                            pl2 = a[1][0].id
                            for rows in list_match:

                                if rows.p1.id == pl1 and rows.p2.id == pl2 or rows.p1.id == pl2 \
                                        and rows.p2.id == pl1:
                                    error += True

                        num = 3
                        while error:

                            print("error2")
                            liste_player = []
                            for pl in list_object:
                                pl1 = pl[0][0]
                                liste_player.append(pl1)
                                pl2 = pl[1][0]
                                liste_player.append(pl2)

                            liste = [0, 1, 2]


                            liste.append(num)
                            new_match.clear()
                            m1 = Match(liste_player[0], 0, liste_player[num], 0)
                            new_match.append(m1.match)
                            r = random.randint(3, 7)

                            while r in liste:
                                r = random.randint(3, 7)
                            print(f"r {r}")
                            liste.append(r)
                            m2 = Match(liste_player[1], 0, liste_player[r], 0)
                            new_match.append(m2.match)
                            r2 = random.randint(3, 7)
                            while r2 in liste:
                                r2 = random.randint(3, 7)
                            print(f"r2 {r2}")
                            liste.append(r2)
                            m3 = Match(liste_player[2], 0, liste_player[r2], 0)
                            new_match.append(m3.match)
                            r3 = 0
                            c = 0
                            for i in range(3, 8):

                                if i not in liste and c == 0:
                                    r3 += i
                                    liste.append(i)
                                    c += 1
                            print(f"r3 {r3}")
                            r4 = 0
                            count = 0
                            for i in range(3, 8):

                                if i not in liste and count == 0:
                                    r4 += i
                                    liste.append(i)
                                    count += 1
                            print(r4)
                            m4 = Match(liste_player[r3], 0, liste_player[r4], 0)
                            new_match.append(m4.match)
                            num += 1
                            print(f"num {num}")
                            liste_player.clear()
                            for a in new_match:

                                pl1 = a[0][0].id
                                pl2 = a[1][0].id
                                for rows in list_match:
                                    if rows.p1.id != pl1 and rows.p2.id != pl2 or rows.p1.id != pl2 \
                                            and rows.p2.id != pl1:
                                        error += False



                    if cc in [2, 6, 10]:

                        error += True
                        while error:

                            liste_player = []
                            for pl in list_object:
                                pl1 = pl[0][0]
                                liste_player.append(pl1)
                                pl2 = pl[1][0]
                                liste_player.append(pl2)

                            liste = [0, 1, 2, 3]
                            new_match.clear()
                            m = Match(liste_player[0], 0, liste_player[1], 0)
                            new_match.append(m.match)
                            r = random.randint(2, 7)
                            while r in liste:
                                r = random.randint(4, 7)
                            liste.append(r)
                            m = Match(liste_player[2], 0, liste_player[r], 0)
                            new_match.append(m.match)
                            r2 = random.randint(4, 7)
                            while r in liste:
                                r2 = random.randint(1, 7)
                            liste.append(r2)
                            m = Match(liste_player[3], 0, list_object[r2], 0)
                            new_match.append(m.match)
                            r3 = 0
                            for i in range(4, 7):
                                if i not in liste:
                                    r3 += i
                                    liste.append(i)
                            r4 = 0
                            for i in range(4, 7):
                                if i not in liste:
                                    r4 += i
                                    liste.append(i)
                            m = Match(liste_player[r3], 0, liste_player[r4], 0)
                            new_match.append(m.match)

                            for a in new_match:

                                pl1 = a[0][0].id
                                pl2 = a[1][0].id
                                for rows in list_match:

                                    if rows.p1.id != pl1 and rows.p2.id != pl2 or rows.p1.id != pl2 \
                                            and rows.p2.id != pl1:
                                        error += False

                    # if cc in [3, 7, 11]:
                    #
                    #     error = True
                    #
                    #     while error:
                    #         liste = [0, 1, 4, 5]
                    #         list_match.clear()
                    #         m = Match(list_object[0], 0, list_object[1], 0)
                    #         list_match.append(m)
                    #         r = random.randint(2, 8)
                    #         while r in liste:
                    #             r = random.randint(1, 7)
                    #         liste.append(r)
                    #         m = Match(list_object[4], 0, list_object[r], 0)
                    #         list_match.append(m)
                    #         r2 = random.randint(2, 8)
                    #         while r in liste:
                    #             r2 = random.randint(2, 8)
                    #         liste.append(r2)
                    #         m = Match(list_object[5], 0, list_object[r2], 0)
                    #         list_match.append(m)
                    #         r3 = 0
                    #         for i in range(2, 8):
                    #             if i not in liste:
                    #                 r3 += i
                    #                 liste.append(i)
                    #         r4 = 0
                    #         for i in range(2, 8):
                    #             if i not in liste:
                    #                 r4 += i
                    #                 liste.append(i)
                    #         m = Match(list_object[r3], 0, list_object[r4], 0)
                    #         list_match.append(m)
                    #
                    #         for a in list_round:
                    #
                    #             pl1 = a[0].player.id
                    #             pl2 = a[1].player.id
                    #             for rows in list_match:
                    #                 if rows.p1.id != pl1 and rows.p2.id != pl2 or rows.p1.id != pl2 \
                    #                         and rows.p2.id != pl1:
                    #                     error += False
                    #
                    # if cc in [4, 8, 12]:
                    #
                    #     error = True
                    #
                    #     while error:
                    #         liste = [0, 1, 6, 7]
                    #         list_match.clear()
                    #         m = Match(list_object[0], 0, list_object[1], 0)
                    #         list_match.append(m)
                    #         r = random.randint(2, 6)
                    #         while r in liste:
                    #             r = random.randint(2, 6)
                    #         liste.append(r)
                    #         m = Match(list_object[5], 0, list_object[r], 0)
                    #         list_match.append(m)
                    #         r2 = random.randint(2, 6)
                    #         while r in liste:
                    #             r2 = random.randint(2, 6)
                    #         liste.append(r2)
                    #         m = Match(list_object[6], 0, list_object[r2], 0)
                    #         list_match.append(m)
                    #         r3 = 0
                    #         for i in range(2, 6):
                    #             if i not in liste:
                    #                 r3 += i
                    #                 liste.append(i)
                    #         r4 = 0
                    #         for i in range(2, 6):
                    #             if i not in liste:
                    #                 r4 += i
                    #                 liste.append(i)
                    #         m = Match(list_object[r3], 0, list_object[r4], 0)
                    #         list_match.append(m)
                    #
                    #         for a in list_round:
                    #
                    #             p1 = a[0].player.id
                    #             p2 = a[1].player.id
                    #             for rows in list_match:
                    #                 if rows[0].player.id != p1 and rows[1].player.id != p2 or rows[
                    #                     0].player.id != p2 \
                    #                         and rows[1].player.id != p1:
                    #                     error += False
        print("end")
        return new_match

    @staticmethod
    def check_match2(id, list_object):

        print("check")
        cc = 0
        list_match = db.get_all_match_by_tournament(id)
        list_match = Match.return_list_obj(list_match)
        new_match = []
        error = False
        for ad in list_object:

            cc += 1
            pl1 = ad[0][0].id
            pl2 = ad[1][0].id
            list_error = []
            for row in list_match:
                if row.p1.id == pl1 and row.p2.id == pl2 or row.p1.id == pl2 and row.p2.id == pl1:
                    if cc in [1, 5, 9]:
                        list_error.append(1)
                    if cc in [2, 6, 10]:
                        list_error.append(2)
                    if cc in [3, 7, 11]:
                        list_error.append(3)
                    if cc in [4, 8, 12]:
                        list_error.append(4)
                    
                    print(cc)
                    # if cc in [1, 5, 9]:
                    #
                    #     print("error")
                    #     new_match.clear()
                    #     m1 = Match(list_object[0][0][0], 0, list_object[1][0][0], 0)
                    #     new_match.append(m1.match)
                    #     m2 = Match(list_object[0][1][0], 0, list_object[1][1][0], 0)
                    #     new_match.append(m2.match)
                    #     m3 = Match(list_object[2][0][0], 0, list_object[2][1][0], 0)
                    #     new_match.append(m3.match)
                    #     m4 = Match(list_object[3][0][0], 0, list_object[3][1][0], 0)
                    #     new_match.append(m4.match)
                    #
                    #     for a in new_match:
                    #
                    #         pl1 = a[0][0].id
                    #         pl2 = a[1][0].id
                    #         for rows in list_match:
                    #
                    #             if rows.p1.id == pl1 and rows.p2.id == pl2 or rows.p1.id == pl2 \
                    #                     and rows.p2.id == pl1:
                    #                 error += True
                    #
                    #     num = 3
                    #     while error:
                    #
                    #         print("error2")
                    #         liste_player = []
                    #         for pl in list_object:
                    #             pl1 = pl[0][0]
                    #             liste_player.append(pl1)
                    #             pl2 = pl[1][0]
                    #             liste_player.append(pl2)
                    #
                    #         liste = [0, 1, 2]
                    #
                    #         liste.append(num)
                    #         new_match.clear()
                    #         m1 = Match(liste_player[0], 0, liste_player[num], 0)
                    #         new_match.append(m1.match)
                    #         r = random.randint(3, 7)
                    #
                    #         while r in liste:
                    #             r = random.randint(3, 7)
                    #         print(f"r {r}")
                    #         liste.append(r)
                    #         m2 = Match(liste_player[1], 0, liste_player[r], 0)
                    #         new_match.append(m2.match)
                    #         r2 = random.randint(3, 7)
                    #         while r2 in liste:
                    #             r2 = random.randint(3, 7)
                    #         print(f"r2 {r2}")
                    #         liste.append(r2)
                    #         m3 = Match(liste_player[2], 0, liste_player[r2], 0)
                    #         new_match.append(m3.match)
                    #         r3 = 0
                    #         c = 0
                    #         for i in range(3, 8):
                    #
                    #             if i not in liste and c == 0:
                    #                 r3 += i
                    #                 liste.append(i)
                    #                 c += 1
                    #         print(f"r3 {r3}")
                    #         r4 = 0
                    #         count = 0
                    #         for i in range(3, 8):
                    #
                    #             if i not in liste and count == 0:
                    #                 r4 += i
                    #                 liste.append(i)
                    #                 count += 1
                    #         print(r4)
                    #         m4 = Match(liste_player[r3], 0, liste_player[r4], 0)
                    #         new_match.append(m4.match)
                    #         num += 1
                    #         print(f"num {num}")
                    #         liste_player.clear()
                    #         for a in new_match:
                    #
                    #             pl1 = a[0][0].id
                    #             pl2 = a[1][0].id
                    #             for rows in list_match:
                    #                 if rows.p1.id != pl1 and rows.p2.id != pl2 or rows.p1.id != pl2 \
                    #                         and rows.p2.id != pl1:
                    #                     error += False
                    #
                    # if cc in [2, 6, 10]:
                    #
                    #     error += True
                    #     while error:
                    #
                    #         liste_player = []
                    #         for pl in list_object:
                    #             pl1 = pl[0][0]
                    #             liste_player.append(pl1)
                    #             pl2 = pl[1][0]
                    #             liste_player.append(pl2)
                    #
                    #         liste = [0, 1, 2, 3]
                    #         new_match.clear()
                    #         m = Match(liste_player[0], 0, liste_player[1], 0)
                    #         new_match.append(m.match)
                    #         r = random.randint(2, 7)
                    #         while r in liste:
                    #             r = random.randint(4, 7)
                    #         liste.append(r)
                    #         m = Match(liste_player[2], 0, liste_player[r], 0)
                    #         new_match.append(m.match)
                    #         r2 = random.randint(4, 7)
                    #         while r in liste:
                    #             r2 = random.randint(1, 7)
                    #         liste.append(r2)
                    #         m = Match(liste_player[3], 0, list_object[r2], 0)
                    #         new_match.append(m.match)
                    #         r3 = 0
                    #         for i in range(4, 7):
                    #             if i not in liste:
                    #                 r3 += i
                    #                 liste.append(i)
                    #         r4 = 0
                    #         for i in range(4, 7):
                    #             if i not in liste:
                    #                 r4 += i
                    #                 liste.append(i)
                    #         m = Match(liste_player[r3], 0, liste_player[r4], 0)
                    #         new_match.append(m.match)
                    #
                    #         for a in new_match:
                    #
                    #             pl1 = a[0][0].id
                    #             pl2 = a[1][0].id
                    #             for rows in list_match:
                    #
                    #                 if rows.p1.id != pl1 and rows.p2.id != pl2 or rows.p1.id != pl2 \
                    #                         and rows.p2.id != pl1:
                    #                     error += False

                    # if cc in [3, 7, 11]:
                    #
                    #     error = True
                    #
                    #     while error:
                    #         liste = [0, 1, 4, 5]
                    #         list_match.clear()
                    #         m = Match(list_object[0], 0, list_object[1], 0)
                    #         list_match.append(m)
                    #         r = random.randint(2, 8)
                    #         while r in liste:
                    #             r = random.randint(1, 7)
                    #         liste.append(r)
                    #         m = Match(list_object[4], 0, list_object[r], 0)
                    #         list_match.append(m)
                    #         r2 = random.randint(2, 8)
                    #         while r in liste:
                    #             r2 = random.randint(2, 8)
                    #         liste.append(r2)
                    #         m = Match(list_object[5], 0, list_object[r2], 0)
                    #         list_match.append(m)
                    #         r3 = 0
                    #         for i in range(2, 8):
                    #             if i not in liste:
                    #                 r3 += i
                    #                 liste.append(i)
                    #         r4 = 0
                    #         for i in range(2, 8):
                    #             if i not in liste:
                    #                 r4 += i
                    #                 liste.append(i)
                    #         m = Match(list_object[r3], 0, list_object[r4], 0)
                    #         list_match.append(m)
                    #
                    #         for a in list_round:
                    #
                    #             pl1 = a[0].player.id
                    #             pl2 = a[1].player.id
                    #             for rows in list_match:
                    #                 if rows.p1.id != pl1 and rows.p2.id != pl2 or rows.p1.id != pl2 \
                    #                         and rows.p2.id != pl1:
                    #                     error += False
                    #
                    # if cc in [4, 8, 12]:
                    #
                    #     error = True
                    #
                    #     while error:
                    #         liste = [0, 1, 6, 7]
                    #         list_match.clear()
                    #         m = Match(list_object[0], 0, list_object[1], 0)
                    #         list_match.append(m)
                    #         r = random.randint(2, 6)
                    #         while r in liste:
                    #             r = random.randint(2, 6)
                    #         liste.append(r)
                    #         m = Match(list_object[5], 0, list_object[r], 0)
                    #         list_match.append(m)
                    #         r2 = random.randint(2, 6)
                    #         while r in liste:
                    #             r2 = random.randint(2, 6)
                    #         liste.append(r2)
                    #         m = Match(list_object[6], 0, list_object[r2], 0)
                    #         list_match.append(m)
                    #         r3 = 0
                    #         for i in range(2, 6):
                    #             if i not in liste:
                    #                 r3 += i
                    #                 liste.append(i)
                    #         r4 = 0
                    #         for i in range(2, 6):
                    #             if i not in liste:
                    #                 r4 += i
                    #                 liste.append(i)
                    #         m = Match(list_object[r3], 0, list_object[r4], 0)
                    #         list_match.append(m)
                    #
                    #         for a in list_round:
                    #
                    #             p1 = a[0].player.id
                    #             p2 = a[1].player.id
                    #             for rows in list_match:
                    #                 if rows[0].player.id != p1 and rows[1].player.id != p2 or rows[
                    #                     0].player.id != p2 \
                    #                         and rows[1].player.id != p1:
                    #                     error += False
        print("end")
        return new_match
