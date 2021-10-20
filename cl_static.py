class static():

    # Define the scales
    ## Define the half tone intervals in a dict
    halfTones = {
        'prime':0,
        'mSekund':1,
        'dSekund':2,
        'mTerz':3,
        'dTerz':4,
        'quart':5,
        'quint':7,
        'mSexte':8,
        'dSexte':9,
        'mSeptime':10,
        'dSeptime':11,
        'oktave':12}

    # Flat and sharp chromatic scale    
    chromScaleF = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']
    chromScaleS = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']

    # Define the Scale Tonalities by half tone steps
    majInt = [2, 2, 1, 2, 2, 2, 1]
    minInt = [2, 1, 2, 2, 1, 2, 2]
    pentInt = [3, 2, 2, 2, 2]
    
    # define the chords-tonalities by intervals
    major =     [
        halfTones['prime'], 
        halfTones['dTerz'], 
        halfTones['quint']]

    minor =     [
        halfTones['prime'], 
        halfTones['mTerz'], 
        halfTones['quint']]
        
    domSept =   [
        halfTones['prime'], 
        halfTones['dTerz'], 
        halfTones['quint'], 
        halfTones['mSeptime']]

    majSept =   [
        halfTones['prime'], 
        halfTones['dTerz'], 
        halfTones['quint'], 
        halfTones['dSeptime']]

    minSept =   [
        halfTones['prime'], 
        halfTones['mTerz'], 
        halfTones['quint'], 
        halfTones['mSeptime']]
    
    def __init__(self):

        # max value of the index
        self.maxInd = len(self.chromScaleS) - 1

        # convenience
        self.chromScale = {"F": self.chromScaleF, "S": self.chromScaleS}
        
        # Put the scales in a dictionary
        self.intervals = {
            "maj":  self.majInt, 
            "min":  self.minInt, 
            "pent": self.pentInt}       

        # put chords in a dict
        self.chords = {
            "maj":  self.major, 
            "min":  self.minor, 
            "dom7": self.domSept, 
            "maj7": self.majSept, 
            "min7": self.minSept}
    
    def sanitizeTone(self, baseTone):

        if type(baseTone) != str:
            raise TypeError("Input must be str not: " + str(type(baseTone)))

        bT = baseTone.capitalize()

        if bT in self.chromScale["F"] or bT in self.chromScale["S"]:
            return bT    
        else: 
            raise ValueError("Invalid input: " + baseTone)
    
    def sanitizeMode(self, mode, type):

        if type(mode) != str:
            raise TypeError("Input must be str not: " + str(type(mode)))

        m = mode.lower()

        if type == "scale":
            modes = list(self.intervals.keys())
        else:
            modes =  list(self.chords.keys())

        if m in modes:
            return m    
        else: 
            raise ValueError("Invalid input: " + mode)

