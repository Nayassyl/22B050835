class Sportsman:
    def __init__(self, sport_id, sport_name):
        self.id = sport_id
        self.name = sport_name
    def printInfo(self):
        print(self.id, self.name)
    def setType(self):
        self.type = input()
    def getType(self):
        print(self.type)
class TeamSport(Sportsman):
    def __init__(self, sport_id, sport_name, num_players):
        super().__init__(sport_id, sport_name)
        self.num = num_players
    def printInfo(self):
        print(self.id, self.name, self.num)

class Football(TeamSport):
    def __init__(self, sport_id, sport_name, num_players, team_name):
        super().__init__(sport_id, sport_name, num_players)
        self.team = team_name
    def printInfo(self):
        print(self.team, self.id, self.name, self.num)

obj1 = Sportsman("00000", "Basketball")
obj1.setType()
obj1.getType()
obj1.printInfo()

obj2 = TeamSport("00000", "Basketball", "5")
obj2.printInfo()

obj3 = Football("00000", "Football", "11", "Bayern")
obj3.printInfo()