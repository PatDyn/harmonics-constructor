# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 21:23:24 2018

@author: Erik
"""

# chord class

class chord():
    
    def __init__(self, baseTone, tonality):
        self.bT = baseTone
        self.t = tonality        
        
        import functions
        
        if 'b' in self.bT  :
            self.uCS = functions.makeChromaticScaleF(self.bT)
        else:
            self.uCS = functions.makeChromaticScale(self.bT)            
        
    def construct(self):
           
        import functions
        
        if self.t == 'M' or self.t == 'D' :
            self.chord = functions.makeMajorChord(self.bT, self.uCS)
        elif self.t == 'm' :
            self.chord = functions.makeMinorChord(self.bT, self.uCS)
        elif self.t == 'dom7' :
            self.chord = functions.makeDomSeptChord(self.bT, self.uCS)
        elif self.t == 'm7' :
            self.chord = functions.makemSeptChord(self.bT, self.uCS)
        elif self.t == 'M7' or self.t == 'D7' : 
            self.chord = functions.makeMSeptChord(self.bT, self.uCS)
    
    def show(self):
        
        if self.t == 'M' :
            print('The major chord:\n', self.chord)
        elif self.t == 'm' :
            print('The minor chord:\n', self.chord)
        elif self.t == 'dom7' :
            print('The dominant 7 chord:\n', self.chord)
        elif self.t == 'm7' :
            print('The minor 7 chord:\n', self.chord)
        elif self.t == 'M7' or self.t == 'D7' : 
            print('The major 7 chord:\n', self.chord)
        
        