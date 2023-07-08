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
    
    def average_age(self):
        total_of_ages = 0
        for follower in self.followers:
            total_of_ages += follower.age
        return total_of_ages/len(self.followers)
    
    def my_followers_mottos(self):
        for follower in self.followers:
            print(f"{follower.life_motto}")

    def least_popular():
        cult_followers = len(Cult.all[0].followers)
        least_popular_cults = []
        for cult in Cult.all:
            if len(cult.followers) <= cult_followers:
                cult_followers = len(cult.followers)
        for cult in Cult.all:
            if len(cult.followers) == cult_followers:
                least_popular_cults.append(cult)
        return least_popular_cults
    #['San Diego, CA', 'Gainsville, FL', 'San Diego, CA']
    def most_common_location():
        list_of_locations = [cult.location for cult in Cult.all]
        number_of_locations = 0
        most_popular = []
        for location in list_of_locations:
            if list_of_locations.count(location) >= number_of_locations:
                number_of_locations = list_of_locations.count(location)
        for location in list_of_locations:
            if list_of_locations.count(location) == number_of_locations and location not in most_popular:
                most_popular.append(location)
        return most_popular



