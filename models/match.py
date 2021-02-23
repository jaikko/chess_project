import random

from models import player, db


class Match:
    match = ()

    def __init__(self, p1, s1, p2, s2):
        self.p1 = p1
        self.p2 = p2
        self.s1 = s1
        self.s2 = s2
        self.match = ([p1, s1], [p2, s2])


class MatchFunction:

    def __init__(self):
        pass

    @staticmethod
    def return_list_obj(liste):
        liste_obj = []
        for g in liste:
            pl1 = player.Player.deserialize(g[0][0])
            score1 = g[0][1]
            pl2 = player.Player.deserialize(g[1][0])
            score2 = g[1][1]

            m = Match(pl1, score1, pl2, score2)
            liste_obj.append(m)
        return liste_obj

    @staticmethod
    def check_match(id, match_obj):

        list_match = db.get_all_match_by_tournament(id)
        list_match = MatchFunction.return_list_obj(list_match)
        error = False
        pl1 = match_obj[0][0].id
        pl2 = match_obj[1][0].id

        for row in list_match:

            if row.p1.id == pl1 and row.p2.id == pl2 or row.p1.id == pl2 and row.p2.id == pl1:
                error = True

        return error

    @staticmethod
    def check_match2(id, list_object):
        print("check")
        cc = 0
        id = id
        list_match = db.get_all_match_by_tournament(id)
        list_match = MatchFunction.return_list_obj(list_match)
        new_match = []
        list_error = []
        error = False
        enter = False

        # trouver les erreurs

        for ad in list_object:

            cc += 1
            pl1 = ad[0][0].id
            pl2 = ad[1][0].id

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

        if not enter:
            if 1 in list_error:

                new_match.clear()
                m1 = Match(list_object[0][0][0], 0, list_object[1][0][0], 0)
                new_match.append(m1.match)
                m2 = Match(list_object[0][1][0], 0, list_object[1][1][0], 0)
                new_match.append(m2.match)
                m3 = Match(list_object[2][0][0], 0, list_object[2][1][0], 0)
                new_match.append(m3.match)
                m4 = Match(list_object[3][0][0], 0, list_object[3][1][0], 0)
                new_match.append(m4.match)

                for x in new_match:
                    pl1 = x[0][0].id
                    pl2 = x[1][0].id

                    for rows in list_match:

                        if rows.p1.id == pl1 and rows.p2.id == pl2 or rows.p1.id == pl2 and rows.p2.id == pl1:
                            error = True

                num = 2
                liste_player = []
                while error:
                    print("error21")
                    for pl in list_object:
                        pl1 = pl[0][0]
                        liste_player.append(pl1)
                        pl2 = pl[1][0]
                        liste_player.append(pl2)
                    new_match.clear()

                    # vérification match1

                    m1 = Match(liste_player[0], 0, liste_player[num], 0)
                    m_status = MatchFunction.check_match(id, m1.match)
                    while m_status:
                        num += 1
                        m1 = Match(liste_player[0], 0, liste_player[num], 0)
                        m_status = MatchFunction.check_match(id, m1.match)

                    error = False
                    new_match.append(m1.match)

                # vérifier les autres matchs

                r_list = [0, 1, 2, num]
                test_match = []
                good_match = 1

                while good_match >= 1:
                    r_list.clear()
                    r_list = [0, 1, 2, num]

                    for pl in list_object:
                        pl1 = pl[0][0]
                        liste_player.append(pl1)
                        pl2 = pl[1][0]
                        liste_player.append(pl2)

                    test_match.clear()

                    # vérification match 2

                    r1 = random.randint(3, 7)
                    while r1 in r_list:
                        r1 = random.randint(3, 7)
                    m2 = Match(liste_player[1], 0, liste_player[r1], 0)
                    m_status = MatchFunction.check_match(id, m2.match)
                    while m_status:
                        r1 = random.randint(3, 7)
                        while r1 in r_list:
                            r1 = random.randint(3, 7)
                        m2 = Match(liste_player[1], 0, liste_player[r1], 0)
                        m_status = MatchFunction.check_match(id, m2.match)
                    r_list.append(r1)
                    test_match.append(m2.match)
                    # print(str(num))
                    # print(f" r1 {r1}")

                    # vérification match 3

                    r2 = random.randint(3, 7)
                    while r2 in r_list:
                        r2 = random.randint(3, 7)
                    m3 = Match(liste_player[2], 0, liste_player[r2], 0)
                    m_status = MatchFunction.check_match(id, m3.match)
                    while m_status:
                        r2 = random.randint(3, 7)
                        while r2 in r_list:
                            r2 = random.randint(3, 7)
                        m3 = Match(liste_player[2], 0, liste_player[r2], 0)
                        m_status = MatchFunction.check_match(id, m3.match)
                    r_list.append(r2)
                    test_match.append(m3.match)

                    # vérification match 4

                    stop = False
                    r3 = 0
                    for i in range(3, 8):
                        if i not in r_list:
                            if not stop:
                                r3 += i
                                stop = True
                    # print(f" r3 {r3}")
                    r_list.append(r3)

                    r4 = 0
                    for i in range(3, 8):
                        if i not in r_list:
                            r4 += i
                    # print(f" r4 {r4}")
                    m4 = Match(liste_player[r3], 0, liste_player[r4], 0)
                    test_match.append(m4.match)

                    # vérifier si les nouveaux matchs sont correctes

                    good_match = 0
                    for b in test_match:

                        pl1 = b[0][0].id
                        pl2 = b[1][0].id
                        for rows in list_match:

                            if rows.p1.id == pl1 and rows.p2.id == pl2 or rows.p1.id == pl2 and rows.p2.id == pl1:
                                good_match += 1

                    if good_match == 0:
                        for i in test_match:
                            new_match.append(i)
                        enter = True

        if not enter:
            if 2 in list_error:
                good_match = 1
                test_match = []
                liste_player = []
                r_list = [0, 1, 2, 3]

                for pl in list_object:
                    pl1 = pl[0][0]
                    liste_player.append(pl1)
                    pl2 = pl[1][0]
                    liste_player.append(pl2)

                while good_match >= 1:
                    r_list.clear()
                    r_list = [0, 1, 2, 3]
                    test_match.clear()
                    new_match.clear()

                    m1 = Match(liste_player[0], 0, liste_player[1], 0)
                    new_match.append(m1.match)

                    # vérification match 2

                    r1 = random.randint(4, 7)
                    while r1 in r_list:
                        r1 = random.randint(4, 7)
                    m2 = Match(liste_player[2], 0, liste_player[r1], 0)
                    m_status = MatchFunction.check_match(id, m2.match)
                    while m_status:
                        r1 = random.randint(4, 7)
                        while r1 in r_list:
                            r1 = random.randint(4, 7)
                        m2 = Match(liste_player[1], 0, liste_player[r1], 0)
                        m_status = MatchFunction.check_match(id, m2.match)
                    r_list.append(r1)
                    test_match.append(m2.match)
                    # print(f" r1 {r1}")

                    # vérification match 3

                    r2 = random.randint(4, 7)
                    while r2 in r_list:
                        r2 = random.randint(4, 7)
                    m3 = Match(liste_player[3], 0, liste_player[r2], 0)
                    m_status = MatchFunction.check_match(id, m3.match)
                    while m_status:
                        r2 = random.randint(4, 7)
                        while r2 in r_list:
                            r2 = random.randint(4, 7)
                        m3 = Match(liste_player[3], 0, liste_player[r2], 0)
                        m_status = MatchFunction.check_match(id, m3.match)
                    r_list.append(r2)
                    test_match.append(m3.match)
                    # print(f" r2{r2}")

                    # vérification match 4

                    stop = False
                    r3 = 0
                    for i in range(4, 8):
                        if i not in r_list:
                            if not stop:
                                r3 = i
                                stop = True
                    # print(f" r3 {r3}")
                    r_list.append(r3)

                    r4 = 0
                    for i in range(4, 8):
                        if i not in r_list:
                            r4 = i
                    # print(f" r4 {r4}")
                    m4 = Match(liste_player[r3], 0, liste_player[r4], 0)
                    test_match.append(m4.match)

                    # vérifier si les nouveaux matchs sont correctes

                    good_match = 0
                    for b in test_match:

                        pl1 = b[0][0].id
                        pl2 = b[1][0].id
                        for rows in list_match:

                            if rows.p1.id == pl1 and rows.p2.id == pl2 or rows.p1.id == pl2 and rows.p2.id == pl1:
                                good_match += 1

                if good_match == 0:
                    for i in test_match:
                        new_match.append(i)
                    enter = True

        if not enter:
            if 3 in list_error:
                good_match = 1
                test_match = []
                liste_player = []
                r_list = [0, 1, 4, 5]

                for pl in list_object:
                    pl1 = pl[0][0]
                    liste_player.append(pl1)
                    pl2 = pl[1][0]
                    liste_player.append(pl2)

                while good_match >= 1:

                    r_list.clear()
                    r_list = [0, 1, 4, 5]
                    test_match.clear()
                    new_match.clear()

                    m1 = Match(liste_player[0], 0, liste_player[1], 0)
                    new_match.append(m1.match)

                    # vérification match 2

                    r1 = random.randint(2, 7)
                    while r1 in r_list:
                        r1 = random.randint(2, 7)
                    m2 = Match(liste_player[4], 0, liste_player[r1], 0)
                    m_status = MatchFunction.check_match(id, m2.match)
                    while m_status:

                        r1 = random.randint(2, 7)
                        while r1 in r_list:
                            r1 = random.randint(2, 7)
                        m2 = Match(liste_player[4], 0, liste_player[r1], 0)
                        m_status = MatchFunction.check_match(id, m2.match)
                    r_list.append(r1)
                    test_match.append(m2.match)
                    # print(f" r1 {r1}")

                    # vérification match 3

                    r2 = random.randint(2, 7)
                    while r2 in r_list:
                        r2 = random.randint(2, 7)
                    m3 = Match(liste_player[5], 0, liste_player[r2], 0)
                    m_status = MatchFunction.check_match(id, m3.match)
                    while m_status:
                        r2 = random.randint(2, 7)
                        while r2 in r_list:
                            r2 = random.randint(2, 7)
                        m3 = Match(liste_player[5], 0, liste_player[r2], 0)
                        m_status = MatchFunction.check_match(id, m3.match)
                    r_list.append(r2)
                    test_match.append(m3.match)
                    # print(f" r2{r2}")

                    # vérification match 4

                    stop = False
                    r3 = 0
                    for i in range(2, 8):
                        if i not in r_list:
                            if not stop:
                                r3 = i
                                stop = True
                    # print(f" r3 {r3}")
                    r_list.append(r3)

                    r4 = 0
                    for i in range(2, 8):
                        if i not in r_list:
                            r4 = i
                    # print(f" r4 {r4}")
                    m4 = Match(liste_player[r3], 0, liste_player[r4], 0)
                    test_match.append(m4.match)

                    # vérifier si les nouveaux matchs sont correctes

                    good_match = 0
                    for b in test_match:

                        pl1 = b[0][0].id
                        pl2 = b[1][0].id

                        for rows in list_match:

                            if rows.p1.id == pl1 and rows.p2.id == pl2 or rows.p1.id == pl2 and rows.p2.id == pl1:
                                good_match += 1

                if good_match == 0:
                    for i in test_match:
                        new_match.append(i)
                    enter = True

        if not enter:
            if 4 in list_error:
                good_match = 1
                test_match = []
                liste_player = []
                r_list = [0, 1, 6, 7]

                for pl in list_object:
                    pl1 = pl[0][0]
                    liste_player.append(pl1)
                    pl2 = pl[1][0]
                    liste_player.append(pl2)

                while good_match >= 1:

                    r_list.clear()
                    r_list = [0, 1, 6, 7]
                    test_match.clear()
                    new_match.clear()

                    m1 = Match(liste_player[0], 0, liste_player[1], 0)
                    new_match.append(m1.match)

                    # vérification match 2

                    r1 = random.randint(2, 7)
                    while r1 in r_list:
                        r1 = random.randint(2, 7)
                    m2 = Match(liste_player[6], 0, liste_player[r1], 0)
                    m_status = MatchFunction.check_match(id, m2.match)
                    while m_status:
                        r1 = random.randint(2, 7)
                        while r1 in r_list:
                            r1 = random.randint(2, 7)
                        m2 = Match(liste_player[6], 0, liste_player[r1], 0)
                        m_status = MatchFunction.check_match(id, m2.match)
                    r_list.append(r1)
                    test_match.append(m2.match)
                    # print(f" r1 {r1}")

                    # vérification match 3

                    r2 = random.randint(2, 7)
                    while r2 in r_list:
                        r2 = random.randint(2, 7)
                    m3 = Match(liste_player[7], 0, liste_player[r2], 0)
                    m_status = MatchFunction.check_match(id, m3.match)
                    while m_status:
                        r2 = random.randint(2, 7)
                        while r2 in r_list:
                            r2 = random.randint(2, 7)
                        m3 = Match(liste_player[7], 0, liste_player[r2], 0)
                        m_status = MatchFunction.check_match(id, m3.match)
                    r_list.append(r2)
                    test_match.append(m3.match)
                    # print(f" r2{r2}")

                    # vérification match 4

                    stop = False
                    r3 = 0
                    for i in range(2, 8):
                        if i not in r_list:
                            if not stop:
                                r3 = i
                    # print(f" r3 {r3}")
                    r_list.append(r3)

                    r4 = 0
                    for i in range(2, 8):
                        if i not in r_list:
                            r4 = i
                    # print(f" r4 {r4}")
                    m4 = Match(liste_player[r3], 0, liste_player[r4], 0)
                    test_match.append(m4.match)

                    # vérifier si les nouveaux matchs sont correctes

                    good_match = 0
                    for b in test_match:

                        pl1 = b[0][0].id
                        pl2 = b[1][0].id
                        for rows in list_match:

                            if rows.p1.id == pl1 and rows.p2.id == pl2 or rows.p1.id == pl2 and rows.p2.id == pl1:
                                good_match += 1

                if good_match == 0:
                    for i in test_match:
                        new_match.append(i)

        return new_match
