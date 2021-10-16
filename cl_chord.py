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
        self.static = static()
        self.bT = baseTone
        self.chord = []
        self.t = ""

    def constructChord(self, mode):

        self.t = mode

        # the base scale
        s = scale(self.bT) 
        userChromScale = s.constructChromScale()
        chord = self.static.chords[mode]

        # step through intervals in the chord
        for interval in chord:         
            self.chord.append(userChromScale[interval%12])

        return self.chord
        
    def show(self):
        
        if self.t == 'maj' :
            print('The major chord:\n', self.chord)
        elif self.t == 'min' :
            print('The minor chord:\n', self.chord)
        elif self.t == 'domS' :
            print('The dominant 7 chord:\n', self.chord)
        elif self.t == 'minS' :
            print('The minor 7 chord:\n', self.chord)
        elif self.t == 'maj7': 
            print('The major 7 chord:\n', self.chord)