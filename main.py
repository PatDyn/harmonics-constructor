# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 20:18:18 2019

@author: Erik
"""

import re

# local imports
from cl_scale import scale
from cl_chord import chord
from cl_static import static

def main():

    stat = static()
    chordModes = list(stat.chords.keys())
    scaleModes = list(stat.intervals.keys())

    print("You can enter Notes from: \n") 
    print(stat.chromScaleF)
    print(stat.chromScaleS)    
    note = str(input("\n Please Enter a Note: "))

    print("Now choose a mode for the scale: \n")    
    print(scaleModes)
    modeScale = str(input("Please choose: "))

    print("Now choose a mode for the chord: \n")    
    print(chordModes)
    modeChord = str(input("Please choose: "))

    
    print("\n")
    s = scale(note)
    s.constructScale(modeScale)
    s.show()

    print("\n")
    c = chord(note)
    c.constructChord(modeChord)
    c.show()


main()



