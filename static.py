# Define the scales
chromScaleS = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'H']
chromScaleF = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Hb', 'H']

# max value of the index
maxInd = len(chromScaleS) - 1

# Define the Scale Intervals
majInt = [2, 2, 1, 2, 2, 2, 1]
minInt = [2, 1, 2, 2, 1, 2, 2]
pentInt = [3, 2, 2, 2, 2]

# Define the half tone intervals
prime = 0
mSekund = 1
dSekund = 2
mTerz = 3
dTerz = 4
quart = 5
quint = 7
mSexte = 8
dSexte = 9
mSeptime = 10
dSeptime = 11
oktave = 12

# define the chords-tonalities
major = [prime, dTerz, quint]
minor = [prime, mTerz, quint]
domSept = [prime, dTerz, quint, mSeptime]
durSept = [prime, dTerz, quint, dSeptime]
mSept = [prime, mTerz, quint, mSeptime]