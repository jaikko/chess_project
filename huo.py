from models import player

pl = player.Player
d = {3: 1, 4: 0.5, 7: 2, 2: 2, 6: 0.5, 8: 2.0, 5: 2, 1: 1}
ll = None
list_score = []
liste_order = pl.ranking_by_score(d)
val = pl.check_same_score(liste_order)
cc = 0
if val:
    liste_order = pl.ranking_by_rank(liste_order)


for k, v in liste_order.items():
    list_score.append(v)

ll = pl.return_list_object(liste_order)

for pla in ll:

    print(pla)
    print(list_score[cc])
    cc +=1