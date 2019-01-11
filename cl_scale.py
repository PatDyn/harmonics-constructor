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
        
    def constructChromScale(self): 
        
        import functions
        
        if 'b' in self.bT  :
            self.uCS = functions.makeChromaticScaleF(self.bT)
        else:
            self.uCS = functions.makeChromaticScale(self.bT)            
            
        return self.uCS
    
    def constructScale(self, cS, tonality): 
        
        import functions 
        
        if tonality == 'm':     
            self.S = functions.makeMinorScale(self.bT, cS)
        elif tonality == 'p':
            self.S = functions.makePentaScale(self.bT, cS)
        elif tonality == 'D' or tonality == 'M':
            self.S = functions.makeMajorScale(self.bT, cS)            
    
        return self.S
        
    #def show(self):