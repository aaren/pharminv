"""python interface to harminv"""
import numpy as np
cimport numpy as np

cimport charminv as charm

cdef class Harminv:
    cdef int n
    cdef np.ndarray signal
    cdef double fmin
    cdef double fmax
    cdef int nf
    cdef charm.harminv_data data

    def __init__(self, n, signal, fmin, fmax, nf):
        self.n = n
        self.signal = signal
        self.fmin = fmin
        self.fmax = fmax
        self.nf = nf

        self.data = self.create_data()

    cdef charm.harminv_data create_data(self):
        return charm.harminv_data_create(self.n, <double complex *> self.signal.data,
                                   self.fmin, self.fmax, self.nf)

    cdef void solve(self):
        charm.harminv_solve(self.data)

    cdef int get_num_freqs(self):
        return charm.harminv_get_num_freqs(self.data)

    cdef double get_freq(self, int k):
        return charm.harminv_get_freq(self.data, k)

    cdef double get_Q(self, int k):
        return charm.harminv_get_Q(self.data, k)

    cdef double get_decay(self, int k):
        return charm.harminv_get_decay(self.data, k)

    cdef double complex get_omega(self, int k):
        return charm.harminv_get_omega(self.data, k)

    cdef double complex get_amplitude(self, int k):
        return charm.harminv_get_amplitude(self.data, k)

    cdef double complex get_freq_error(self, int k):
        return charm.harminv_get_freq_error(self.data, k)
