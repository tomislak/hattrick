#!/usr/bin/python3
# https://github.com/PiGo86/pychpp
from pychpp import CHPP

consumer_key = 'dpf43f3p2l4k3l03'
concumer_secret = 'kd94hf93k423kf44'

chpp = CHPP(consumer_key, concumer_secret)

auth = chpp.get_auth()

print(auth)

# code = ''