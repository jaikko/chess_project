from Models import models
from Controller import Controller

print("Bonjour Que voulez-vous faire?")
print("1.Ajouter joueur")
print("2. Créer un tournoi")
choice = input("Indiquez le numéro de l'action: ")


Controller.action_choice(choice)


# list_player = []
# player1 = models.Player(1, 'test1', "", "", "", "10")
# player2 = models.Player(2, 'test2', "", "", "", "12")
# player3 = models.Player(3, 'test3', "", "", "", "14")
# player4 = models.Player(4, 'test4', "", "", "", "16")
#
# for i in range(1, 5):
#     player = models.Player(i, 'test' + str(i), "", "", "", 10 + i)
#     list_player.append(player)
#
# liste = sorted(list_player, key=lambda player: player.rank, reverse=True)
#
# listeA = liste[0:2]
# listeB = liste[2:4]
#
# match = models.Match(listeA[0], listeB[0])
# roundd = models.Round(1, match)
# tournament = models.Tournament("test", "ghjkl", "fgh", roundd)


