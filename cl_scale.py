# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 00:07:28 2019



@author: Erik
"""

class scale():    
    
    def __init__(self, baseTone):
        self.bT = baseTone        
        self.uCS = []
        self.S = []
        self.constructChromScale()
        
    def constructChromScale(self): 
        
        import functions
        
        if 'b' in self.bT  :
            self.uCS = functions.makeChromaticScaleF(self.bT)
        else:
            self.uCS = functions.makeChromaticScale(self.bT)            
            
    def constructScale(self, tonality): 
        
        import functions 
        
        self.t = tonality
        
        if tonality == 'm':     
            self.S = functions.makeMinorScale(self.bT, self.uCS)
        elif tonality == 'p':
            self.S = functions.makePentaScale(self.bT, self.uCS)
        elif tonality == 'D' or tonality == 'M':
            self.S = functions.makeMajorScale(self.bT, self.uCS)            
        
    def show(self):        
        
        if self.t == 'm':     
            print('The minor scale:\n', self.S)
        elif self.t == 'p':
            print('The pentatonic scale:\n', self.S)
        elif self.t == 'D' or self.t == 'M':
            print('The major scale:\n', self.S)            