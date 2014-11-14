import numpy as np

import harminv

# print dir(harminv)

time = np.arange(1000)
signal = np.cos(time) + np.cos(3*time)

harm = harminv.Harminv(signal=signal, fmin=0.01, fmax=100, nf=100)

# print dir(harm)
print signal.size
print harm.n
# print harm.fmin
# print harm.fmax
print harm.nf
harm.solve()

print harm.get_num_freqs()
# print harm.get_freq(0)
# print harm.get_freq(1)
# print harm.get_freq(2)

# print harm.get_freq_error(0)
# print harm.get_freq_error(1)
# print harm.get_freq_error(2)

# print harm.get_amplitude(0)
# print harm.get_amplitude(1)
# print harm.get_amplitude(2)

print "extracting..."
freq = harm.extract('freq', np.double)
print freq
print "extracted."
# print harm.freq
harm.set()
print harm.freq
print harm.freq[0]
print dir(harm.freq)
