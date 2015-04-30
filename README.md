pharminv
========

This is a python interface to [harminv], a library for performing
harmonic inversion on a signal.

[harminv]: http://ab-initio.mit.edu/wiki/index.php/Harminv

### Requirements:

- BLAS & LAPACK
- libharminv-dev
- numpy

### Installation:

Make sure that you have the requirements above, then

```
pip install pharminv
```

#### Installing libharminv

On Debian / Ubuntu this is available with

```bash
sudo apt-get install libharminv-dev
```

Otherwise you'll need to build it yourself. Download the sources
from [here](http://ab-initio.mit.edu/harminv/harminv-1.4.tar.gz).

You need to install libharminv somewhere that python can find it at
runtime. This should happen by default (installs to `/usr/local`),
but you may need to change this to `/usr`:

    PREFIX=/usr

If you have the `python-config` tool available you can determine the
prefix with 

    PREFIX=`python-config --prefix`

Now install with the following:

```bash
./configure --with-pic --enable-shared --prefix=$PREFIX
make
make install
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

### License:

[harminv] was written by Steven G. Johnson and is licensed under the
GNU GPLv2+, copyright 2005 by the Massachusetts Institute of Technology.

This python interface to harminv is licensed under the standard BSD
3-clause license.
