import ipdb
from lib import *

# test your code here
# e.g.

f1 = Follower( 'Emiley', 31, 'Living the Dream' )
f2 = Follower( 'Peter', 35, 'Nice guys finish last.' )
f3 = Follower( 'Bowski', 37, 'I take being silly very seriously.' )
f4 = Follower( 'Eric', 37, "yep" )
c1 = Cult( 'Heavens Gate', 'San Diego, CA', 1974, 'Human Metamorphosis' )
c2 = Cult( 'QAnon', 'Gainsville, FL', 2020, 'TRUMP IS GOD!' )
c3 = Cult( 'Pi Cult', 'Mars, PA', 2016, 'Math is power, math is might. Math will make your future bright!' )
# c4 = Cult( 'Hells Gate', 'San Diego, CA', 1974, 'Human Metamorphosis' )
# c5 = Cult( 'Purgatorys Gate', 'Parksville, NY', 1974, 'Human Metamorphosis' )
# c6 = Cult( 'Earths Gate', 'Boston, MA', 1974, 'Human Metamorphosis' )

bo1 = BloodOath( '2019-09-16', f1, c1 )
bo2 = BloodOath( '2021-11-21', f4, c2 )
bo3 = BloodOath( '2016-03-14', f2, c3 )
bo4 = BloodOath( '2020-03-18', f3, c3 )
bo5 = BloodOath( '2020-03-18', f1, c2 )
bo6 = BloodOath( '2020-03-18', f1, c3 )
bo7 = BloodOath( '2020-04-18', f3, c1 )
bo8 = BloodOath( '2018-03-01', f2, c1 )



# c1.followers => ???
# f1.cults => ???




print( "Mwahahaha!" )
ipdb.set_trace()