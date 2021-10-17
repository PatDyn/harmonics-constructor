# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 00:07:28 2019

@author: Erik
"""

from cl_static import static

## Helper Function: sanitize
## accepts a base tone, string
## returns the base tone if in chromatic_scale
## or returns an error message

def sanitize(baseTone):

    if baseTone in static.chromScaleF or baseTone in static.chromScaleS:
        return baseTone
    else: 
        raise ValueError("The input: " + baseTone + " was invalid")

class scale():    
    
    def __init__(self, baseTone):

        self.bT = sanitize(baseTone)
        self.stat = static() 
        self.S = []

    def chromScalePicker(self): 

        if 'b' in self.bT:
            mode = 'F'
        elif self.bT == 'C' or self.bT == 'D' or self.bT == 'F' or self.bT == 'G':
            mode = 'F'
        else:
            mode = 'S'
            
        return mode

    def constructChromScale(self):

        ## Get the mode of the Chromatic Scale
        modeSwitch = self.chromScalePicker()

        ## Generate scales from input
        chromScaleLocal = self.stat.chromScale[modeSwitch]
        index = chromScaleLocal.index(self.bT)

        if index == 0: # is the base tone the first note in the scale?
            userChromScale = chromScaleLocal
        elif index == len(chromScaleLocal)-1: # or is it the last?
            userChromScale = [*[chromScaleLocal[index]], *chromScaleLocal[0:index]] 
        else:
            userChromScale = [*chromScaleLocal[index:12], *chromScaleLocal[0:index]]

        return userChromScale
            
    # makeScale: constructs a scale from input
    # accepts a base tone, a type switch for the kind of scale
    # returns a list of characters 

    def constructScale(self, mode): 

        self.mode = mode
        userChromScale = self.constructChromScale()

        # from the type switch, get the interval-scheme 
        # with the chromatic scale from before, we return the correct scale
        interval_skips = self.stat.intervals[mode]

        # null-entry is the base tone
        self.S = [self.bT]

        # indices following the base tone
        index = userChromScale.index(self.bT)

        # make the scale
        for interval in interval_skips: # 

            index = index + interval

            self.S.append(userChromScale[index%12]) 

        return self.S
        
    def show(self):        
        
        if self.mode == 'min':     
            print('The minor scale:\n', self.S)
        elif self.mode == 'pent':
            print('The pentatonic scale:\n', self.S)
        elif self.mode == 'maj':
            print('The major scale:\n', self.S)            