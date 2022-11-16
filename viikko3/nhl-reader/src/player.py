class Player:
    def __init__(self, name, nationality, goals, assists, team):
        self.name = name
        self.nationality = nationality
        self.goals = goals
        self.assists = assists
        self.team = team
        self.points = self.goals + self.assists
    
    def __str__(self):
        return f"{self.name:20} {self.team:2} {self.goals:3} +{self.assists:3} ={self.points:4}"
