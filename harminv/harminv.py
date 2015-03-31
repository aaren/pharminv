import numpy as np

import _harminv


class Harminv(_harminv.Harminv):
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
