import time
import random
import pickle
import pdb
pdb.set_trace()
playerlevel = 1
playermission = 1
level = pickle.dump(playerlevel, open("playerlevel","wb"))
mission = pickle.dump(playermission, open("playermission","wb"))

intro = 'Welcome to WWII: Battle Warriors!\nPlease set up your username and password for this game so your data is saved at the bottom of the message!\nWe are glad to see you here!'
print(intro)
while True:
