# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 21:23:24 2018

@author: Erik
"""

from cl_static import static
from cl_scale import scale



# chord class

class chord():
    
    def __init__(self, baseTone):

        self.stat = static()
        self.bT = self.stat.sanitizeTone(baseTone)

    def constructChord(self, mode):

        # Every time constructChord is called, we construct a new chord
        self.chord = []
        self.mode = self.stat.sanitizeMode(mode)

        # create the base scale
        s = scale(self.bT) 
        userChromScale = s.constructChromScale()

        chord = self.stat.chords[self.mode]

        # step through intervals in the chord
        for interval in chord:         
            self.chord.append(userChromScale[interval%12])

        return self.chord
        
    def show(self):
        
        if self.mode == "maj" :
            print("The " + self.bT + " major chord:\n", self.chord)
        elif self.mode == "min" :
            print("The " + self.bT + " minor chord:\n", self.chord)
        elif self.mode == "dom7" :
            print("The " + self.bT + " dominant 7 chord:\n", self.chord)
        elif self.mode == "min7" :
            print("The " + self.bT + " minor 7 chord:\n", self.chord)
        elif self.mode == "maj7": 
            print("The " + self.bT + " major 7 chord:\n", self.chord)