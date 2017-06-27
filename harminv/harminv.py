import numpy as np

from . import charminv


class Harminv(charminv.Harminv):
    threshold = {'error': 0.1,
                 'relative_error': np.inf,
                 'amplitude': 0.0,
                 'relative_amplitude': -1.0,
                 'Q': 10.0
                 }

    def compute_threshold(self, inrange=False):
        rel_amp = self.amplitude.max() * self.threshold['relative_amplitude']
        rel_err = self.error.min() * self.threshold['relative_error']

        ok = (((not inrange) |
              ((self.fmin < self.freq) & (self.fmax > self.freq)))
              & (self.error <= self.threshold['error'])
              & (self.error <= rel_err)
              & (self.amplitude >= self.threshold['amplitude'])
              & (self.amplitude >= rel_amp)
              & (np.abs(self.Q) > self.threshold['Q']))

        return ok

    @property
    def modes(self):
        t = np.arange(self.signal.size) * self.dt
        return self.compute_modes(t)

    def compute_modes(self, time):
        modes = self.amplitude * np.exp(-1j * (2 * np.pi * self.freq
                                               * time[None].T - self.phase)
                                        - self.decay * time[None].T)
        return modes.T

def invert(signal, fmin, fmax, dt=1, nf=100):
    """Compute the *Harmonic Inversion* of the given signal.

    Returns a numpy recarray, with the results of the inversion
    available as attributes.

    Usage:

    import harminv

    tau = 2 * np.pi
    time = np.linspace(0, 1, 1000)
    signal = np.cos(12 * tau * time) + np.cos(5 * tau * time)

    inversion = harminv.invert(signal, fmin=2, fmax=100, dt=0.001)

    # access the frequencies
    inversion.frequency

    # access the amplitudes
    inversion.amplitudes

    # reconstruct the signal
    components = (inversion.amplitude
                    * np.exp(-1j * (2 * np.pi
                                    * inversion.frequency
                                    * time[:, None] - inversion.phase)
                                    - inversion.decay * time[:, None]))

    reconstruction = components.sum(axis=1)
    """
    harm = Harminv(signal, fmin=fmin, fmax=fmax, dt=dt, nf=nf)

    array_names = [(harm.freq,      'frequency'),
                   (harm.amplitude, 'amplitude'),
                   (harm.phase,     'phase'),
                   (harm.decay,     'decay'),
                   (harm.Q,         'Q'),
                   (harm.error,     'error')]

    arrays, names = zip(*array_names)

    return np.rec.fromarrays(arrays, names=names)
