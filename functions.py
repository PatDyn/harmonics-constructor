# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 01:04:57 2019

This is a helper file for creating scales and chords outside of classes.
The functions will be used in the respective classes.
This is done for more flexibility in handling stuff.

@author: Erik
"""

## Below are the functions for the creation of Scales 

def makeChromaticScale(baseTone):

    import static
    ind = static.chromScaleS.index(baseTone)
    userChromScale = [static.chromScaleS[ind]]

    for i in range(1,len(static.chromScaleS)): # count from 0 to the end of the list
        chromInd = ind + i
        if chromInd > static.maxInd: # check if we exceed the index of the chromatic scale list
            cnInd = chromInd - 12  # go back to the note that is within the index range
            userChromScale.append(static.chromScaleS[cnInd]) # append the found note to the scale
        else:
            userChromScale.append(static.chromScaleS[chromInd])
    
    return userChromScale

def makeChromaticScaleF(baseTone):

    import static
    ind = static.chromScaleF.index(baseTone)
    userChromScaleF = [static.chromScaleF[ind]]

    for i in range(1,len(static.chromScaleF)): # count from 0 to the end of the list
        chromInd = ind + i
        if chromInd > static.maxInd: # check if we exceed the index of the chromatic scale list
            cnInd = chromInd - 12  # go back to the note that is within the index range
            userChromScaleF.append(static.chromScaleF[cnInd]) # append the found note to the scale
        else:
            userChromScaleF.append(static.chromScaleF[chromInd])
    
    return userChromScaleF


# makeScale: constructs a scale from input
# accepts a base tone, a type switch for the kind of scale
# returns a list of characters 

def makeScale(baseTone, typeSwitch): 

    import static

    if 'b' in baseTone:
        userChromScale = makeChromaticScaleF(baseTone)
    else:
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


def makeMajorScale(baseTone, userChromScale):

    import static
    
    if 'b' in baseTone:
        userChromScale = makeChromaticScaleF(baseTone)
    
    ind = userChromScale.index(baseTone)
    userMajorScale = [userChromScale[ind]]
    
    # make the major scale
    for i in range(0,len(static.majInt)-1): # count from 0 to the end of the list
        ind = ind + static.majInt[i] # add the interval of majInt to ind and accumulate the values, also offset due to python counting
        # print(majInt[i])
        userMajorScale.append(userChromScale[ind]) # append the found note to the scale
        
    return userMajorScale

def makeMinorScale(baseTone, userChromScale):
    
    import static
    
    if baseTone == 'C' or baseTone == 'D' or baseTone == 'F' or baseTone == 'G' or baseTone == 'Hb':
        userChromScale = makeChromaticScaleF(baseTone)
        
    ind = userChromScale.index(baseTone)
    userMinorScale = [userChromScale[ind]]
    
    # make the minor scale
    for i in range(0,len(static.minInt)-1): # count from 0 to the end of the list
        ind = ind + static.minInt[i] # add the interval of minInt to ind and accumulate the values, also offset due to python counting
        # print(majInt[i])
        userMinorScale.append(userChromScale[ind]) # append the found note to the scale
        
    return userMinorScale

def makePentaScale(baseTone, userChromScale):
    
    import static
    
    if 'b' in baseTone:
        userChromScale = makeChromaticScaleF(baseTone)
    
    ind = userChromScale.index(baseTone)
    userPentaScale = [userChromScale[ind]]
    
    # make the pentatonic scale
    for i in range(0,len(static.pentInt)-1): # count from 0 to the end of the list
        ind = ind + static.pentInt[i] # add the interval of pentInt to ind and accumulate the values, also offset due to python counting
        # print(majInt[i])
        userPentaScale.append(userChromScale[ind]) # append the found note to the scale
        
    return userPentaScale

## Here come the chords, currently Major, minor, Major Seven, minor Seven and Dominant Seven

def makeMajorChord(baseTone, userChromScale):
    
    import static
    userMajChord = []
    
    # get the chord
    for i in range(0,len(static.major)): # count through 0 to the end of the list
        ind = static.major[i] 
        if ind > static.maxInd: # check if we exceed the index of the chromatic scale list
            nInd = ind - 12 # if this is the case subtract len(chromScale) from ind
            userMajChord.append(userChromScale[nInd]) # append the found note to the scale
        else:
            userMajChord.append(userChromScale[ind]) # append the found note to the scale
        
    return userMajChord

def makeMinorChord(baseTone, userChromScale):
    
    import static
    userMinChord = []
    
    # get the chord
    for i in range(0,len(static.minor)): # count through 0 to the end of the list
        ind = static.minor[i] 
        if ind > static.maxInd: # check if we exceed the index of the chromatic scale list
            nInd = ind - 12 # if this is the case subtract len(chromScale) from ind
            userMinChord.append(userChromScale[nInd]) # append the found note to the scale
        else:
            userMinChord.append(userChromScale[ind]) # append the found note to the scale
        
    return userMinChord

def makeMSeptChord(baseTone, userChromScale):
    
    import static
    userMSeptChord = []
    
    # get the chord
    for i in range(0,len(static.durSept)): # count through 0 to the end of the list
        ind = static.durSept[i] 
        if ind > static.maxInd: # check if we exceed the index of the chromatic scale list
            nInd = ind - 12 # if this is the case subtract len(chromScale) from ind
            userMSeptChord.append(userChromScale[nInd]) # append the found note to the scale
        else:
            userMSeptChord.append(userChromScale[ind]) # append the found note to the scale
        
    return userMSeptChord

def makemSeptChord(baseTone, userChromScale):
    
    import static
    usermSeptChord = []
    
    # get the chord
    for i in range(0,len(static.mSept)): # count through 0 to the end of the list
        ind = static.mSept[i] 
        if ind > static.maxInd: # check if we exceed the index of the chromatic scale list
            nInd = ind - 12 # if this is the case subtract len(chromScale) from ind
            usermSeptChord.append(userChromScale[nInd]) # append the found note to the scale
        else:
            usermSeptChord.append(userChromScale[ind]) # append the found note to the scale
        
    return usermSeptChord

def makeDomSeptChord(baseTone, userChromScale):
    
    import static
    userDomSeptChord = []
    
    # get the chord
    for i in range(0,len(static.domSept)): # count through 0 to the end of the list
        ind = static.domSept[i] 
        if ind > static.maxInd: # check if we exceed the index of the chromatic scale list
            nInd = ind - 12 # if this is the case subtract len(chromScale) from ind
            userDomSeptChord.append(userChromScale[nInd]) # append the found note to the scale
        else:
            userDomSeptChord.append(userChromScale[ind]) # append the found note to the scale
        
    return userDomSeptChord