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

    cdef public double [:] freq

    def __init__(self, signal, fmin, fmax, nf):
        self.n = signal.size
        self.signal = signal
        self.fmin = fmin
        self.fmax = fmax
        # TODO: set a default value for nf
        self.nf = nf

        self.data = self.create_data()

    cdef charminv.data create_data(self):
        return charminv.data_create(self.n, <double complex *> self.signal.data,
                                    self.fmin, self.fmax, self.nf)

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
        nf = self.get_num_freqs()
        array = np.empty((nf,), dtype)

        for i in range(nf):
            array[i] = getattr(self, 'get_' + thing)(i)

        return array

    cpdef set(self):
        self.freq = self.extract('freq', np.double)

    # cpdef np.ndarray freq(self):
        # nf = self.get_num_freqs()
        # # # for each nf, extract the properties and set as attributes
        # return np.fromiter((self.get_freq(i) for i in range(nf)),
                           # dtype=np.double)
