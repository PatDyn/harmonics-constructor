# -*-C coding: utf-8 -*-
"""
Created on Thu Jan  3 00:52:22 2019

@author: Erik
"""

from cl_scale import scale
from cl_chord import chord

# Get the base tone from input
bT = True #input('The Base Tone: ')

s = scale(bT)

s.constructScale('min')
s.show()

s.constructScale('maj')
s.show()

s.constructScale('pent')
s.show()

c = chord(bT)
c.constructChord('maj')
c.show()

c.constructChord('majS')
c.show()

c.constructChord('min')
c.show()

c.constructChord('domS')
c.show()

c.constructChord('minS')
c.show()