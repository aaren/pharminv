from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

setup(
    name='harminv',
    version='0.1',
    description='Python interface to harminv',
    py_modules=['harminv'],
    author="Aaron O'Leary",
    install_requires=['numpy', 'cython'],
    ext_modules=cythonize([Extension('harminv',
                                     ["harminv.pyx"],
                                     libraries=['harminv'])])
)
