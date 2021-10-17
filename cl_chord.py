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

    def constructChord(self, mode):

        # Every time constructChord is called, we construct a new chord
        self.chord = []
        self.mode = mode

        # create the base scale
        s = scale(self.bT) 
        userChromScale = s.constructChromScale()

        chord = self.static.chords[mode]

        # step through intervals in the chord
        for interval in chord:         
            self.chord.append(userChromScale[interval%12])

        return self.chord
        
    def show(self):
        
        if self.mode == 'maj' :
            print('The major chord:\n', self.chord)
        elif self.mode == 'min' :
            print('The minor chord:\n', self.chord)
        elif self.mode == 'domS' :
            print('The dominant 7 chord:\n', self.chord)
        elif self.mode == 'minS' :
            print('The minor 7 chord:\n', self.chord)
        elif self.mode == 'majS': 
            print('The major 7 chord:\n', self.chord)