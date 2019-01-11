# -*-C coding: utf-8 -*-
"""
Created on Thu Jan  3 00:52:22 2019

@author: Erik
"""

from functions import *
from static import *

# Get the base tone from input
bT = input('The Base Tone: ')

ind = chromScaleS.index(bT)

# init the scales
userMajorScale = [chromScaleS[ind]]
userMinorScale = [chromScaleS[ind]]
userChromScale = [chromScaleS[ind]]
userMajChord = [chromScaleS[ind]]
maxInd = len(chromScaleS) - 1

userChromScale = makeChromaticScale(bT)

# make the chromatic scale
#for i in range(1,len(chromScaleS)): # count from 0 to the end of the list
#    chromInd = ind + i
#    if chromInd > maxInd: # check if we exceed the index of the chromatic scale list
#        cnInd = chromInd - 12  
#        userChromScale.append(chromScaleS[cnInd]) # append the found note to the scale
#    else:
#        userChromScale.append(chromScaleS[chromInd])

# make the scale
#for i in range(0,len(majInt)): # count from 0 to the end of the list
#    ind = ind + majInt[i] # add the interval of majint to ind and accumulate the values, also offset due to python counting
#    print(ind)
#    if ind >= maxInd: # check if we exceed the index of the chromatic scale list
#        nInd = ind - 12 # if this is the case subtract len(chromScale) from ind
#        userMajorScale.append(chromScaleS[nInd]) # append the found note to the scale
#    else:
#        userMajorScale.append(chromScaleS[ind])    

ind = userChromScale.index(bT)
# make the major scale
for i in range(0,len(majInt)-1): # count from 0 to the end of the list
    ind = ind + majInt[i] # add the interval of majint to ind and accumulate the values, also offset due to python counting
    # print(majInt[i])
    userMajorScale.append(userChromScale[ind]) # append the found note to the scale
    
ind = userChromScale.index(bT)
# make the minor scale
for i in range(0,len(minInt)-1): # count from 0 to the end of the list
    ind = ind + minInt[i] # add the interval of majint to ind and accumulate the values, also offset due to python counting
    userMinorScale.append(userChromScale[ind]) # append the found note to the scale
                    
# get the chord
for i in range(1,len(major)): # count through 0 to the end of the list
    ind = major[i] # add the interval of majint to ind and accumulate the values
    if ind > maxInd: # check if we exceed the index of the chromatic scale list
        nInd = ind - 12 # if this is the case subtract len(chromScale) from ind
        userMajChord.append(userChromScale[nInd]) # append the found note to the scale
    else:
        userMajChord.append(userChromScale[ind])


print('The chromatic scale:\n', userChromScale)
print('The major scale:\n', userMajorScale)
#print('The minor scale:\n', userMinorScale)
print('The Chord:\n', userMajChord)