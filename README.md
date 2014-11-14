pharminv
========

This is a python interface to [harminv], a library for performing
harmonic inversion on a signal.

[harminv]: http://ab-initio.mit.edu/wiki/index.php/Harminv

### Requirements:

- BLAS & LAPACK
- harminv
- cython, numpy

### Installation:

Make sure that you have the requirements above, then

```
python setup.py install
```

### Usage:

```python
import numpy as np
import harminv

time = np.arange(1000)
signal = np.cos(time) + np.cos(3*time)

harm = harminv.Harminv(signal=signal, fmin=0.01, fmax=100, nf=100)

harm.freq        # mode frequencies
harm.decay       # decay rates
harm.Q           # Q factor
harm.amplitudes  # absolute amplitudes
harm.phase       # phase shift 
```
