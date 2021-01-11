from models import tournament

class Tournament:


    def __init__(self, name, place, date, obj=Round):
        self.name = name
        self.place = place
        self.date = date
        self.match = obj
