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
    note = str(input("\nPlease Enter a Note: "))

    print("Now choose a mode for the scale: ")    
    print(scaleModes)
    modeScale = str(input("\nPlease choose: "))
    s = scale(note)
    s.constructScale(modeScale)

    print("Now choose a mode for the chord: ")    
    print(chordModes)
    modeChord = str(input("\nPlease choose: "))
    c = chord(note)
    c.constructChord(modeChord)
    
    print("\n")
    s.show()

    print("\n")
    c.show()


main()



