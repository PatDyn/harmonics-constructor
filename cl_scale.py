# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 00:07:28 2019

@author: Erik
"""

class scale():

from static import *
from functions import makeChromaticScale
    
    def __init__(self, b, t):
        self.bT = b
        self.T = t
        
    def construct(self): 
        chromScale = makeChromaticScale(self.bT)
        userMajorScale = [chromScaleS[ind]]
        userMinorScale = [chromScaleS[ind]]
        
        ind = chromScale.index(self.bT)
        # make the major scale
        for i in range(0,len(majInt)-1): # count from 0 to the end of the list
            ind = ind + majInt[i] # add the interval of majint to ind and accumulate the values, also offset due to python counting
            # print(majInt[i])
            userMajorScale.append(userChromScale[ind]) # append the found note to the scale
    
        ind = chromScale.index(self.bT)
        # make the minor scale
        for i in range(0,len(minInt)-1): # count from 0 to the end of the list
            ind = ind + minInt[i] # add the interval of majint to ind and accumulate the values, also offset due to python counting
            userMinorScale.append(userChromScale[ind]) # append the found note to the scale
        
    def show(self):