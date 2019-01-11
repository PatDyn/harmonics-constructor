# -*-C coding: utf-8 -*-
"""
Created on Thu Jan  3 00:52:22 2019

@author: Erik
"""



from functions import *
from static import *
from cl_scale import scale

# Get the base tone from input
bT = 'C' #input('The Base Tone: ')

s = scale(bT)
userChromScale = s.constructChromScale()
userMinorScale = s.constructScale(userChromScale, 'm')
userMajorScale = s.constructScale(userChromScale, 'D')
userPentaScale = s.constructScale(userChromScale, 'p')

#userMajChord = makeMajorChord(bT, userChromScale)

print('The chromatic scale:\n', userChromScale)
print('The major scale:\n', userMajorScale)
print('The minor scale:\n', userMinorScale)
print('The pentatonic scale:\n', userPentaScale)
#print('The Major Chord:\n', userMajChord)