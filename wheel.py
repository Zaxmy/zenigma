#!/usr/bin/env python3
from collections import deque
from random import shuffle

__author__ = "Johan Zaxmy"
__copyright__ = "Copyright 2019"
__license__ = "GPL"
__version__ = "1.0.0"
__maintainer__ = "Johan Zaxmy"
__email__ = "johan@zaxmy.com"
__status__ = "Production"

class Wheel(deque):
    def __init__(self,size=0):
        super(Wheel,self).__init__(maxlen=size)
        for i in range(0,size):
            self.append(i)
        shuffle(self)
        self.pos = 0
        self.did360 = False

    def index(self,val):
        tmp = [A for A in self]
        return(tmp.index(val))

    def rotate(self,n=1):
        self.did360 = False
        self.pos += n
        if self.pos > self.maxlen:
            self.pos %= self.maxlen
            self.did360 = True
        super(Wheel,self).rotate(n)

    def zero(self):
        super(Wheel,self).rotate(self.maxlen-self.pos)
        self.pos = 0
        self.did360 = False


class Enigma():
    def __init__(self,wheels=3,steps=1,initial=[0,0,0]):
        self.wheels = []
        for _ in range(0,wheels):
            self.wheels.append(Wheel(size=26))
        self.setWheelPosition(initial)
        self.step = steps

    def setWheelPosition(self,positions=[0,0,0]):
        for (w,p) in zip(self.wheels,positions):
            w.zero()
            w.rotate(p)

    def encode(self,letter):
        num = ord(letter.upper())-ord('A')
        for w in self.wheels:
            num = w[num] 
        return(chr(num+ord('A')))

    def decode(self,letter):
        ind = ord(letter)-ord('A')
        for w in range(len(self.wheels)-1,-1,-1):
            ind = self.wheels[w].index(ind)
        return(chr(ind+ord('A')))
    
    def rotate(self):
        if len(self.wheels):
            self.wheels[0].rotate(self.step)
            for w in range(1,len(self.wheels)):
                if self.wheels[w-1].did360 :
                    self.wheels[w].rotate(self.step)
    def zero(self):
        for w in self.wheels:
            w.zero()

    def print(self):
        out = []
        for a in range(0,26):
            out.append("%s->%2d " % (chr(a+ord('A')),self.wheels[0][a]))
        for w in range(1,len(self.wheels)-1):
            for a in range(0,26):
                out[a] += "%2d->%2d " % (a,self.wheels[w][a])
        for a in range(0,26):
            out[a] += ("%2d->%s" % (a, chr(self.wheels[len(self.wheels)-1][a]+ord('A'))))
        for l in out:
            print(l)

        


