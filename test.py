from models import db, player
from collections import OrderedDict

pl = player.Player

dicts = {4: 1, 3: 1, 2: 0, 1: 0}

list_no_same = []
new_liste = []
lsss = []
score = ""

# for key, value in dicts.items():
#
#     if score == value:
#         list_same.append(key)
#         list_same.append(old_id)
#         print("meme")
#     if score != value:
#         if len(list_same) > 1:
#             for i in list_same:
#                 json = db.get_player_by_id(i)
#                 obj = pl.deserialize(json)
#                 new_liste[obj.rank] = int(obj.id)
#
#             for k in sorted(new_liste.keys(), reverse=False):
#                 print(k)
#                 json = db.get_player_by_id(k)
#                 obj = pl.deserialize(json)
#                 lsss[obj.id] = int(obj.rank)
#                 print(f"id: {obj.id} nom: {obj.last_name} prenom: {obj.first_name}")
#
#                 print("ok")
#             print(lsss)
#         list_same.clear()
#     score = value
#     old_id = key
#     print(value)
#
# print(list_same)
# id_old = ""
# d2 = ""
# sat = False
# value = ""
# for key, value in dicts.items():
#     if key not in list_same:
#         value = value
#
#         if key not in list_same:
#             if value == value:
#                 list_same.append(key)
#             if value != value:
#                 sat += True
#             if sat:
#                 for i in list_same:
#                     json = db.get_player_by_id(i)
#                     obj = pl.deserialize(json)
#                     dd[obj.rank] = obj.id
#                 d2 = OrderedDict(sorted(dd.items(), key=lambda t: t[0], reverse=True))
#                 print(d2)
#                 for ke, ve in d2.items():
#                     print(ve)
#                     lsss.append(ve)
# json = db.get_player_by_id(ve)
# obj = pl.deserialize(json)
# print(f"id: {obj.id} nom: {obj.last_name} prenom: {obj.first_name} rank: {obj.rank}")
all = []
old_id = ""
old_value = ""
count = 0
d2 =""
list_same = []
dd = {}
for k, v in dicts.items():
    count += 1
    if k not in list_same:
        if old_value == v:
            list_same.append(k)
            list_same.append(old_id)
            if count == 4:
                for i in list_same:
                    json = db.get_player_by_id(i)
                    obj = pl.deserialize(json)
                    dd[obj.rank] = obj.id
                    d2 = OrderedDict(sorted(dd.items(), key=lambda t: t[0], reverse=True))
                    print(d2)
                for ke, va in d2.items():
                    all.append(va)
                d2.clear()
                dd.clear()
                list_same.clear()
        if old_value != v:

            if len(list_same) > 1:
                for i in list_same:
                    json = db.get_player_by_id(i)
                    obj = pl.deserialize(json)
                    dd[obj.rank] = obj.id
                    d2 = OrderedDict(sorted(dd.items(), key=lambda t: t[0], reverse=True))
                    print(d2)

                for ke, va in d2.items():
                    all.append(va)
                d2.clear()
                dd.clear()
                list_same.clear()
    old_id = k
    old_value = v

print(all)

for i in all:
    json = db.get_player_by_id(i)
    obj = pl.deserialize(json)
    print(f"id: {obj.id} nom: {obj.last_name} prenom: {obj.first_name} rank: {obj.rank}")

# for o in list_same:
#     json = db.get_player_by_id(o)
#     obj = pl.deserialize(json)
#     print(f"id: {obj.id} nom: {obj.last_name} prenom: {obj.first_name} rank: {obj.rank}")
