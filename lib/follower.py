from .bloodoath import BloodOath

class Follower:
    all = []

    def __init__(self, name, age, life_motto):
        self.name = name
        self.age = age
        self.life_motto = life_motto
        Follower.all.append(self)
        
    def __repr__(self):
        return f"<Name: {self.name}  Motto: {self.life_motto}"