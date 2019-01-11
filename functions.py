# -*- coding: utf-8 -*-
"""
Created on Thu Jan  3 01:04:57 2019

@author: Erik
"""

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

def makeMajorScale(baseTone, userChromScale):

    import static
    ind = userChromScale.index(baseTone)
    userMajorScale = [userChromScale[ind]]
    
    # make the major scale
    for i in range(0,len(static.majInt)-1): # count from 0 to the end of the list
        ind = ind + static.majInt[i] # add the interval of majint to ind and accumulate the values, also offset due to python counting
        # print(majInt[i])
        userMajorScale.append(userChromScale[ind]) # append the found note to the scale
        
    return userMajorScale

def makeMinorScale(baseTone, userChromScale):
    
    import static
    
    if baseTone == 'C' or baseTone == 'D' or baseTone == 'F' or baseTone == 'G' or baseTone == 'Hb':
        userChromScale = makeChromaticScaleF(baseTone)
        
    ind = userChromScale.index(baseTone)
    userMinorScale = [userChromScale[ind]]
    
    # make the major scale
    for i in range(0,len(static.minInt)-1): # count from 0 to the end of the list
        ind = ind + static.minInt[i] # add the interval of majint to ind and accumulate the values, also offset due to python counting
        # print(majInt[i])
        userMinorScale.append(userChromScale[ind]) # append the found note to the scale
        
    return userMinorScale

def makeMajorChord(baseTone, userChromScale):
    
    import static
    #ind = userChromScale.index(baseTone)
    #userMajChord = [userChromScale[ind]]
    userMajChord = []
    
    # get the chord
    for i in range(0,len(static.major)): # count through 0 to the end of the list
        ind = static.major[i] # add the interval of majint to ind and accumulate the values
        if ind > static.maxInd: # check if we exceed the index of the chromatic scale list
            nInd = ind - 12 # if this is the case subtract len(chromScale) from ind
            userMajChord.append(userChromScale[nInd]) # append the found note to the scale
        else:
            userMajChord.append(userChromScale[ind])
        
    return userMajChord