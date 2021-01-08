import View.View as V
import Module.Db as Db



def action_choice(choice):
    if choice == "1":
        id = Db.get_id_player()
        player = V.add_player(id)
        player = Db.serialize_player(player)
        Db.add_db(player)

    if choice == "2":
        V.add_tournament()

    if choice == "3":

        Db.get_player_by_id(1)