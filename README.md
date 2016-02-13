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

See [below](#installing-libharminv) for help with installing
harminv.

### Usage:

`harminv.invert` contains the basic functionality of the harminv
tool. This function should remain stable but the API elsewhere is
subject to change.

```python
import numpy as np
import harminv

time = np.linspace(0, 1, 1000)

signal = np.cos(2 * np.pi * time * 10) + np.cos(2 * np.pi * time * 20)

inversion = harminv.invert(signal, fmin=1, fmax=100, dt=0.001)

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

### Installing libharminv

On Debian / Ubuntu this is available with

```bash
sudo apt-get install libharminv-dev
```

Otherwise you'll need to build it yourself. Download the sources
from [here](http://ab-initio.mit.edu/harminv/harminv-1.4.tar.gz).

You need to install libharminv somewhere that python can find it at
runtime. This should happen by default (installs to `/usr/local`),
but you may need to change this to `/usr`:

```bash
PREFIX=/usr
```

Now install with the following:

```bash
./configure --with-pic --enable-shared --prefix=$PREFIX
make
make install
```

#### User installation

If you don't have admin rights on your system you'll need to install
to a directory that you have access to. Here I'll assume that is
`$HOME/.local`.

Here is how I do it (using Anaconda python with the mkl libraries on
CentOS 5):

```bash
./configure --with-pic --enable-shared --prefix=$HOME/.local --with-blas=$HOME/.local/lib/libopenblas.so
make
make install
```

Note that I've linked to openblas. I installed this separately. If
you have BLAS/LAPACK installed on your system elsewhere you might
not need to do this. There might be a way to link against Anaconda
mkl libraries but I don't know what it is.

Now you need to set `LD_LIBRARY_PATH` to include your directory. I
have this in my bashrc:

```bash
export LD_LIBRARY_PATH=$HOME/.local
```

Finally, when you install pharminv, you need to tell pip where to
look for your installation of libharminv:

```bash
CFLAGS="-I$HOME/.local/include -L$HOME/.local/lib" pip install pharminv
```
