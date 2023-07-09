class BloodOath:
    all = []

    def __init__(self, initiation_date, follower, cult):
        self.initiation_date = initiation_date
        self.follower = follower
        self.cult = cult
        BloodOath.all.append(self)
        cult.recruit_follower(follower)
        follower.join_cult(cult)

    def first_oath():
        # from follower import Follower
        # oath_date = ""
        # first_follower = Follower
        def get_oath_date(oath):
            return oath.initiation_date
        sorted_list = sorted(BloodOath.all, key=get_oath_date)
        return sorted_list[0].follower
