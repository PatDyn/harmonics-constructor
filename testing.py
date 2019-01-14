# -*-C coding: utf-8 -*-
"""
Created on Thu Jan  3 00:52:22 2019

@author: Erik
"""



from functions import *
from static import *
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