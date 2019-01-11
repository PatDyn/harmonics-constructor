# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 00:07:28 2019

@author: Erik
"""

class scale():

import static
import functions
    
    def __init__(self, baseTone, tonality):
        self.bT = baseTone
        self.T = tonality
        
    def constructChromScale(self): 
        
        if 
        
        ind = static.chromScaleS.index(self.bT)
        userChromScale = [static.chromScaleS[ind]]

        for i in range(1,len(static.chromScaleS)): # count from 0 to the end of the list
            chromInd = ind + i
            if chromInd > static.maxInd: # check if we exceed the index of the chromatic scale list
               cnInd = chromInd - 12  # go back to the note that is within the index range
               userChromScale.append(static.chromScaleS[cnInd]) # append the found note to the scale
            else:
               userChromScale.append(static.chromScaleS[chromInd])
    
    
        
    def constructMajScale(self): 
        cScale = makeChromaticScale(self.bT)
        uMajorScale = [chromScaleS[ind]]
        userMinorScale = [chromScaleS[ind]]
        
    def constructMinScale(self): 
        cScale = makeChromaticScale(self.bT)
        uMajorScale = [chromScaleS[ind]]
        userMinorScale = [chromScaleS[ind]]
        
    def show(self):