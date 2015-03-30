import numpy as np

import harminv

# print dir(harminv)

tau = 2 * np.pi
dt = 0.01
time = np.arange(1000) * dt
noise = 0.1 * np.random.random(1000)
signal = noise + np.cos(tau * 0.1 * time) + np.cos(tau * 0.3 * time) + np.cos(tau * 0.5 * time)

with open('tests/input.dat', 'w') as f:
    signal.tofile(f, sep=' ')

harm = harminv.Harminv(signal=signal, fmin=0.001, fmax=1, nf=100)

# modes are accepted if Q > 10 and error < 0.1
limit = (harm.error < 0.1) & (harm.Q > 10)

for i in range(harm.freq[limit].size):
    print("%g, %e, %g, %g, %g, %e" % (harm.freq[limit][i],
                                      harm.decay[limit][i],
                                      harm.Q[limit][i],
                                      harm.amplitude[limit][i],
                                      harm.phase[limit][i],
                                      harm.error[limit][i]))
