import numpy as np

import harminv

# print dir(harminv)

time = np.arange(1000)
signal = np.cos(time) + np.cos(3*time)

harm = harminv.Harminv(signal=signal, fmin=0.01, fmax=100, nf=100)

print harm.freq
print harm.freq[0]
