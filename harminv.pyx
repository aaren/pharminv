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
    cdef charminv.data data

    def __init__(self, signal, fmin, fmax, nf):
        self.n = signal.size
        self.signal = signal
        self.fmin = fmin
        self.fmax = fmax
        self.nf = nf

        self.data = self.create_data()

    cdef charminv.data create_data(self):
        return charminv.data_create(self.n, <double complex *> self.signal.data,
                                    self.fmin, self.fmax, self.nf)

    cpdef solve(self):
        charminv.solve(self.data)

    cpdef get_num_freqs(self):
        return charminv.get_num_freqs(self.data)

    cpdef get_freq(self, int k):
        return charminv.get_freq(self.data, k)

    cpdef get_Q(self, int k):
        return charminv.get_Q(self.data, k)

    cpdef get_decay(self, int k):
        return charminv.get_decay(self.data, k)

    cpdef complex get_omega(self, int k):
        return charminv.get_omega(self.data, k)

    cpdef complex get_amplitude(self, int k):
        return charminv.get_amplitude(self.data, k)

    cpdef complex get_freq_error(self, int k):
        return charminv.get_freq_error(self.data, k)
