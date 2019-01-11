# -*-C coding: utf-8 -*-
"""
Created on Thu Jan  3 00:52:22 2019

@author: Erik
"""



from functions import *
from static import *

# Get the base tone from input
bT = 'C' #input('The Base Tone: ')

userChromScale = makeChromaticScale(bT)  
userMajorScale = makeMajorScale(bT, userChromScale)
userMinorScale = makeMinorScale(bT, userChromScale)
userMajChord = makeMajorChord(bT, userChromScale)

print('The chromatic scale:\n', userChromScale)
print('The major scale:\n', userMajorScale)
print('The minor scale:\n', userMinorScale)
print('The Major Chord:\n', userMajChord)