from tinydb import TinyDB, Query


def get_player_by_id():
    db = TinyDB("db.json")
    table = db.table("players")
    user = Query()
    result = table.search(user.id == "1")
    print("re" + str(result))

get_player_by_id()