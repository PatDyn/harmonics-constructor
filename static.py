# Define the scales
chromScaleS = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'H']
chromScaleF = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Hb', 'H']

# Put the chromatic scales in a dictionary

chromScale = {"F":chromScaleF, "S":chromScaleS}

# max value of the index
maxInd = len(chromScaleS) - 1

# Define the Scale Intervals
majInt = [2, 2, 1, 2, 2, 2, 1]
minInt = [2, 1, 2, 2, 1, 2, 2]
pentInt = [3, 2, 2, 2, 2]
# more scales to come

# Put the intervals into a dictionary
intervals = {"maj":majInt, "min":minInt, "pent":pentInt}

# Define the half tone intervals in a dict
halfTones = {'prime':0,'mSekund':1,'dSekund':2,'mTerz':3,'dTerz':4,'quart':5,'quint':7,'mSexte':8,'dSexte':9,'mSeptime':10,'dSeptime':11,'oktave':12}

# define the chords-tonalities
major =     [halfTones['prime'], halfTones['dTerz'], halfTones['quint']]
minor =     [halfTones['prime'], halfTones['mTerz'], halfTones['quint']]
domSept =   [halfTones['prime'], halfTones['dTerz'], halfTones['quint'], halfTones['mSeptime']]
majSept =   [halfTones['prime'], halfTones['dTerz'], halfTones['quint'], halfTones['dSeptime']]
minSept =   [halfTones['prime'], halfTones['mTerz'], halfTones['quint'], halfTones['mSeptime']]

# put them in a dict for easy access
chords_dict = {"maj":major, "min":minor, "domS":domSept, "majS":majSept, "minS":minSept}