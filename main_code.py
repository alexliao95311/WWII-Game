import time
import random
import pickle
import pdb
playerlevel = 1
playermission = 1
level = pickle.dump(playerlevel, open("playerlevel.dat","wb"))
mission = pickle.dump(playermission, open("playermission.dat","wb"))

intro = 'Welcome to WWII: Battle Warriors!\nPlease sign in for this game so your data is saved!\nWe are glad to see you here!'
time.sleep(2)
print(intro)
time.sleep(2)
while True:
    user = 'alexliao'
    password = 95311
    user_1 = input('Enter your username: ')
    password_1 = int(input('Enter your password: '))
    if user == user_1 and password == password_1:
        print('Welcome, alexlia0_destroyer12!')
        time.sleep(2)
        break
    else:
        print('Sorry, that username and/or password is incorrect. Please retry:')
        time.sleep(1)
        continue

print('Loading game... Please wait patiently.')
time.sleep(3.8)
