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

def makeMajorScale(baseTone):

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
    
    return userMajorScale