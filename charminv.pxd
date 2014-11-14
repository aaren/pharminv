cdef extern from "complex.h":
    pass

cdef extern from "harminv.h":
    ctypedef struct data "harminv_data":
        pass

    data data_create "harminv_data_create" (int n, double complex *signal,
                                            double fmin, double fmax, int nf)

    void solve "harminv_solve" (data d)
    int get_num_freqs "harminv_get_num_freqs" (data d)

    double get_freq "harminv_get_freq" (data d, int k)
    double get_Q "harminv_get_Q" (data d, int k)
    double get_decay "harminv_get_decay" (data d, int k)

    double complex get_omega "harminv_get_omega" (data d, int k)
    double complex get_amplitude "harminv_get_amplitude" (data d, int k)

    double get_freq_error "harminv_get_freq_error" (data d, int k)
