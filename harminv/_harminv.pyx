"""python interface to harminv"""
import numpy as np
cimport numpy as np

cimport charminv

cdef class Harminv:
    cdef readonly int n
    cdef readonly np.ndarray signal
    cdef readonly double fmin
    cdef readonly double fmax
    cdef readonly int nf
    cdef readonly double dt
    cdef charminv.data data

    cdef public np.ndarray freq
    cdef public np.ndarray Q
    cdef public np.ndarray decay
    cdef public np.ndarray omega
    cdef public np.ndarray amplitude
    cdef public np.ndarray phase
    cdef public np.ndarray error

    def __init__(self, signal, fmin, fmax, nf, dt=1.0):
        """Perform Harmonic Inversion on the given signal.

        Assuming that the signal is comprised of a sum of sinusoids
        (i.e.  modes), extract their frequencies, amplitudes and
        decay rates (for exponentially decaying sinusoids).

        Sets these attributes:

            freq - the mode frequencies
            decay - the exponential decay constants
            Q - the decay lifetime (as in Q-factor)
            amplitude - the (real, positive) amplitudes
            omega - the complex angular frequencies
            phase - the phase shifts (radians)
            error - an estimate of the error in the frequencies

        Then the signal can be reconstructed with

            amplitude * exp[-i * (2 pi freq t - phase) - decay t]
        """
        self.n = signal.size
        self.signal = signal.astype(np.complex128)
        self.fmin = fmin
        self.fmax = fmax
        # TODO: set a default value for nf
        self.nf = nf
        self.dt = dt

        self.data = self.create_data()
        self.solve()
        self.extract_all()

    cdef charminv.data create_data(self):
        return charminv.data_create(self.n,
                                    <double complex *> self.signal.data,
                                    self.dt * self.fmin,
                                    self.dt * self.fmax,
                                    self.nf)

    cpdef solve(self):
        charminv.solve(self.data)

    cpdef int get_num_freqs(self):
        return charminv.get_num_freqs(self.data)

    cpdef double get_freq(self, int k):
        return charminv.get_freq(self.data, k)

    cpdef double get_Q(self, int k):
        return charminv.get_Q(self.data, k)

    cpdef double get_decay(self, int k):
        return charminv.get_decay(self.data, k)

    cpdef complex get_omega(self, int k):
        return charminv.get_omega(self.data, k)

    cpdef complex get_amplitude(self, int k):
        return charminv.get_amplitude(self.data, k)

    cpdef double get_freq_error(self, int k):
        return charminv.get_freq_error(self.data, k)

    cpdef extract(self, thing, dtype):
        """Extract a single output from the harminv data
        object. Returns an array with the given dtype.
        """
        nf = self.get_num_freqs()
        array = np.empty((nf,), dtype)
        for i in range(nf):
            array[i] = getattr(self, 'get_' + thing)(i)
        return array

    cpdef extract_all(self):
        """Extract all of the outputs from the Harminv data object."""
        self.freq = self.extract('freq', np.double) / self.dt
        self.omega = self.extract('omega', np.complex)

        self.decay = self.extract('decay', np.double) / self.dt
        self.Q = self.extract('Q', np.double)

        amplitude = self.extract('amplitude', np.complex)
        self.amplitude = np.abs(amplitude)
        self.phase = np.angle(amplitude)

        self.error = self.extract('freq_error', np.double)
