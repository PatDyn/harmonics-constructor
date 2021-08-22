# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 21:23:24 2018

@author: Erik
"""

# chord class

class chord():
    
    def __init__(self, baseTone):
        self.bT = baseTone
               
        import functions
        
        self.uCS = functions.makeChromaticScale(self.bT)            
        
    def constructChord(self, tonality):
           
        import functions
        self.t = tonality 

        self.chord = functions.makeChord(self.bT, self.t)
    
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