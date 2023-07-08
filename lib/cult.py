from .bloodoath import BloodOath

class Cult:
    all = []
    
    def __init__(self, name, location, founding_year, slogan):
        self.name = name
        self.location = location
        self.founding_year = founding_year
        self.slogan = slogan
        Cult.all.append(self)
        self.followers = []

    def __repr__(self):
         return f"Cult Name: {self.name}  Slogan: {self.slogan}"

    def recruit_follower(self, follower):
            self.followers.append(follower)

    def cult_population(self):
        return len(self.followers)

    def find_by_name(name):
        for cult in Cult.all:
            if cult.name == name:
                return cult
        return f"{name} does not exist. Maybe start it youself?"
    
    def find_by_location(location):
        for cult in Cult.all:
            if cult.location == location:
                return cult
        return f"No cults exist in {location}"
    
    def find_by_founding_year(year):
        for cult in Cult.all:
            if cult.founding_year == year:
                return cult
        return f"No cults started in {year}"