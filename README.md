pharminv
========

This is a python interface to [harminv], a library for performing
harmonic inversion on a signal.

[harminv]: http://ab-initio.mit.edu/wiki/index.php/Harminv

### Requirements:

- BLAS & LAPACK
- libharminv-dev
- cython, numpy

### Installation:

Make sure that you have the requirements above, then

```
pip install harminv
```

### Usage:

`harminv.invert` contains the basic functionality of the harminv
tool. This function should remain stable but the API elsewhere is
subject to change.

```python
import numpy as np
import harminv

time = np.linspace(0, 1, 1000)

signal = np.cos(2 * np.pi * time * 10) + np.cos(2 * np.pi * time * 20)

inversion = harminv.invert(signal, fmin=1, fmax=100)

inversion.freq        # mode frequencies
inversion.decay       # decay rates
inversion.Q           # Q factor
inversion.amplitudes  # absolute amplitudes
inversion.phase       # phase shift 
```
