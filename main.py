# -*- coding: utf-8 -*-
"""
Created on Mon Jan 14 20:18:18 2019

main script with UI stuff

User can choose:
    The Base Tone
        Needs a check, if a valid Base Tone is given
    The scales to show (multiple possible)
        Chromatic
        Major
        Minor
        Pentatonic
        (others?)
    The Chords to show 
        Major
        Minor
        Dom7
        M7
        m7

@author: Erik
"""

import re

# local imports
from appJar import gui
from cl_scale import scale
from cl_chord import chord
from static import chromScaleF
from static import chromScaleS

app = gui()

app.addLabel("title", "Please enter a Base Tone")
app.addLabelEntry("Base Tone")

def press(button):
    val = None
    if button == "Cancel":
        app.stop()
    else:
        val = app.getEntry("Base Tone")
        
    return val

app.addButtons(["Submit", "Cancel"], press)
app.setFocus("Base Tone")

app.go()

bT = press("Base Tone")


# print("The base tone:", bT)
# Get the base tone from input
# bT = input('The Base Tone: ')

# check if a character was entered

if bT.isalpha():
    bTtemp = re.search("^[a-zA-Z]", bT) 
    bTtemp = bTtemp[0]
    bTtemp = bTtemp.upper()
else:
    print("ERROR: Please Enter a note from the following chromatic scales:")
    print(chromScaleF)
    print(chromScaleS)

bTtemp2 = re.search("[b #]", bT)

# print("bTtemp2:", bTtemp2)

if bTtemp2 != None:
    if bTtemp2.isalpha():
        bTtemp2 = bTtemp2[0]
        bTtemp2 = bTtemp2.lower()
        bT = bTtemp + bTtemp2
    else:
        print("ERROR: Please Enter a note from the following chromatic scales:")
        print(chromScaleF)
        print(chromScaleS)


        
#print('2nd Part of bT:' + bTtemp2)


#if bTtemp.isupper() == False: # Input Check - first if uppercase or lowercase
#    bTtemp = bTtemp.swapcase()
    
       
# deconstruct bT
# check first char of bT for case
# check second char of bT for case


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