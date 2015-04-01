import subprocess

from setuptools import setup, Extension

from Cython.Build import cythonize

try:
    pandoc = subprocess.Popen(['pandoc', 'README.md', '--to', 'rst'],
                              stdout=subprocess.PIPE)
    readme = pandoc.communicate()[0]

except OSError:
    with open('README.md') as f:
        readme = f.read()

setup(
    name='pharminv',
    version="0.2.0",
    description='Python interface to harminv',
    long_description=readme,
    packages=['harminv'],
    author="Aaron O'Leary",
    author_email='dev@aaren.me',
    license='GPLv3',
    url='http://github.com/aaren/harminv',
    install_requires=['numpy', 'cython'],
    ext_modules=cythonize([Extension('harminv.charminv',
                                     ["harminv/charminv.pyx"],
                                     libraries=['harminv'])])
)
