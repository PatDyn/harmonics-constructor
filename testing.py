# -*-C coding: utf-8 -*-
"""
Created on Thu Jan  3 00:52:22 2019

@author: Erik
"""

from cl_scale import scale
from cl_chord import chord

# Get the base tone from input
bT = 'C' #input('The Base Tone: ')

s = scale(bT)

s.constructScale('m')
s.show()

s.constructScale('D')
s.show()

s.constructScale('p')
s.show()

c = chord(bT, 'M')
c.construct()
c.show()

#userMajChord = makeMajorChord(bT, userChromScale)
#print('The Major Chord:\n', userMajChord)

# makeScale: constructs a scale from input
# accepts a base tone, a type switch for the kind of scale
# returns a list of characters 

def makeScale(baseTone, typeSwitch): 

    import static
       
    # so we need to check the input of the user 
    # 1. is there a 'b' contained in the input 
    # use a chromatic scale with flat notes as half tone steps as base
     
    # 2. otherwise we use the 'normal' chromatic scale 

    if 'b' in baseTone:
        userChromScale = makeChromaticScaleF(baseTone)

    # from the mode selector, get the interval-scheme 
    # with the chromatic scale from before, we return the correct scale

    index = userChromScale.index(baseTone)
    userScale = [userChromScale[index]]
    
    # make the scale
    for interval in intervals: # count from 0 to the end of the list
         # add the interval of majInt to ind and accumulate the values, also offset due to python counting
        index = index + intervals[interval]
        # print(majInt[i])
        userScale.append(userChromScale[index]) # append the found note to the scale
        
    return userScale