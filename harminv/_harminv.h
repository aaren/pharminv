// Wrapper for harminv to maintain api compatibility
// across versions 1.3 and 1.4
# include <harminv.h>

#if HARMINV_VERSION_MAJOR < 1 || (HARMINV_VERSION_MAJOR == 1 && HARMINV_VERSION_MINOR < 4)
#  define harminv_get_amplitude(pa, d, k) *(pa) = harminv_get_amplitude(d, k)
#  define harminv_get_omega(pw, d, k) *(pw) = harminv_get_omega(d, k)
#endif
