import numpy as np

import harminv

# print dir(harminv)

tau = 2 * np.pi
dt = 0.01
time = np.arange(1000) * dt
noise = 0.1 * np.random.random(1000)
signal = noise + np.cos(tau * 0.1 * time) + np.cos(tau * 0.3 * time) + np.cos(tau * 0.5 * time)

with open('input.dat', 'w') as f:
    signal.tofile(f, sep=' ')

harm = harminv.Harminv(signal=signal, fmin=0.05, fmax=1, nf=100)

print harm.freq
print harm.error
# print harm.freq[0]

# sorted = np.abs(harm.amplitude).argsort()
