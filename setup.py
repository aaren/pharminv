from setuptools import setup
from setuptools import Extension
from Cython.Build import cythonize

setup(
    name='harminv',
    version='0.1',
    description='Python interface to harminv',
    packages=['harminv'],
    author="Aaron O'Leary",
    install_requires=['numpy', 'cython'],
    ext_modules=cythonize([Extension('harminv._harminv',
                                     ["harminv/_harminv.pyx"],
                                     libraries=['harminv'])])
)
