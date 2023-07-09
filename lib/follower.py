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
        return f"<Name: {self.name}  Motto: {self.life_motto}>"
    
    def join_cult(self, cult):          #Ask Adam if deliverable was worded incorrectly
        self.cults.append(cult)

    def of_a_certain_age(age):
        return [follower for follower in Follower.all if follower.age >= age]
    
    def my_cults_slogans(self):
        for oath in BloodOath.all:
            if oath.cult in self.cults and oath.follower == self:
                print(oath.cult.slogan)

    def most_active():
        cult_count = 0
        most_cults = []
        for follower in Follower.all:
            if len(follower.cults) > cult_count:
                cult_count = len(follower.cults)
        for follower in Follower.all:
            if len(follower.cults) == cult_count:
                most_cults.append(follower)
        return most_cults
    
    
    def top_ten():
        def get_cult_count(follower):
            return len(follower.cults)
        sorted_list = sorted(Follower.all, key=get_cult_count, reverse = True)
        return sorted_list
        

