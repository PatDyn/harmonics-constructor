# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 01:04:57 2019

This is a helper file for creating scales and chords outside of classes.
The functions will be used in the respective classes.
This is done for more flexibility in handling stuff.

@author: Erik
"""

## Below are the functions for the creation of Scales 

## Helper Function: chromScalePicker
## accepts a base tone, string
## returns a string, S or F depending on the base tone

def chromScalePicker(baseTone): 
    
    if 'b' in baseTone:
        mode = 'F'
    elif baseTone == 'C' or baseTone == 'D' or baseTone == 'F' or baseTone == 'G' or baseTone == 'Hb':
        mode = 'F'
    else:
        mode = 'S'
    
    return mode

## Function: make ChromaticScale
## accepts a base tone and a string "S" or "F"
## Returns a list of strings, with sharp or flat notes
## TODO: Check user input!

def makeChromaticScale(baseTone):

    ## Import constants from static
    import static

    ## Get the mode of the Chromatic Scale
    modeSwitch = chromScalePicker(baseTone)

    ## Generate scales from input
    chromScaleLocal = static.chromScale[modeSwitch]
    index = chromScaleLocal.index(baseTone)

    if index == 0: # is the base tone the first note in the scale?
        userChromScale = chromScaleLocal
    elif index == len(chromScaleLocal)-1: # or is it the last?
        userChromScale = chromScaleLocal[index] + chromScaleLocal[0:index] 
    else:
        userChromScale = chromScaleLocal[index:12] + chromScaleLocal[0:index-1]
    return userChromScale
    
# makeScale: constructs a scale from input
# accepts a base tone, a type switch for the kind of scale
# returns a list of characters 

def makeScale(baseTone, typeSwitch): 

    import static

    userChromScale = makeChromaticScale(baseTone)

    # from the type switch, get the interval-scheme 
    # with the chromatic scale from before, we return the correct scale
    interval_skips = static.intervals[typeSwitch]

    # null-entry is the base tone
    index = userChromScale.index(baseTone)
    userScale = [userChromScale[index]]
    
    # make the scale
    for interval in interval_skips: # 
        index = index + interval
        userScale.append(userChromScale[index%12]) 
        
    return userScale

## Here come the chords, currently Major, minor, Major Seven, minor Seven and Dominant Seven
# makeChord: construct a chord from a base tone and a type
# accepts a string base tone and a string type switch
# returns a list of strings containing the notes making up the chord

def makeChord(baseTone, typeSwitch):
    
    import static

    # the initial tone
    userChord = []

    # the base scale
    userChromScale = makeChromaticScale(baseTone)
    chord = static.chords_dict[typeSwitch]
    
    index = 0

    # step through intervals in the chord
    for interval in chord:         
        userChord.append(userChromScale[interval%12])
        
    return userChord

