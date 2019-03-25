#!/usr/bin/env python3

from wheel import Wheel
from wheel import Enigma
import random

__author__ = "Johan Zaxmy"
__copyright__ = "Copyright 2019"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Johan Zaxmy"
__email__ = "johan@zaxmy.com"
__status__ = "Production"

random.seed(a="JOHAN",version=2)
WHEELS=20
DASHES=(WHEELS*7)-3
e = Enigma(wheels=WHEELS)

#for letter in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
#    encoded = e.encode(letter)
#    decoded = e.decode(encoded)
#    print("Letter [%s] Encoded [%s] Decoded [%s]" % (letter,encoded,decoded))
    
#for i in range(0,200):
#    encoded = e.encode('A')
#    print("Letter [A] Encoded [%s]" % (encoded))
#    e.rotate()
msg=""
e.zero()
print("Wheels\n%s"%("-"*DASHES))
e.print()
print("%s"%("-"*DASHES))
print("Initial wheel positions")
init = [random.randint(0,25) for _ in range(0,len(e.wheels))]
print(init,sep=',')
e.setWheelPosition(init)
print("%s"%("-"*DASHES))

msg=""
for letter in "EXAMPLEXSENTENCEXTOXBEXENCODED":
    msg += e.encode(letter)
    e.rotate()
print("Encoded [%s]" % (msg))
e.setWheelPosition(init)
dec=""
for letter in msg:
    dec += e.decode(letter)
    e.rotate()
print("Decoded [%s]" % (dec))
