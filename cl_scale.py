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
        
        self.uCS = functions.makeChromaticScale(self.bT)
            
    def constructScale(self, mode): # create a scale
        
        import functions 

        self.mode = mode        
        self.S = functions.makeScale(self.bT, self.mode)
        
    def show(self):        
        
        if self.mode == 'min':     
            print('The minor scale:\n', self.S)
        elif self.mode == 'pent':
            print('The pentatonic scale:\n', self.S)
        elif self.mode == 'maj':
            print('The major scale:\n', self.S)            