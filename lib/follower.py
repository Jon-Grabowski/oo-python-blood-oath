from .bloodoath import BloodOath

class Follower:
    all = []

    def __init__(self, name, age, life_motto):
        self.name = name
        self.age = age
        self.life_motto = life_motto
        Follower.all.append(self)
        self.cults = []
        
    def __repr__(self):
        return f"<Name: {self.name}  Motto: {self.life_motto}"
    
    def join_cult(self, cult):          #Ask Adam if deliverable was worded incorrectly
        self.cults.append(cult)

    def of_a_certain_age(age):
        return [follower for follower in Follower.all if follower.age >= age]