import subprocess

from setuptools import setup, Extension

try:
    pandoc = subprocess.Popen(['pandoc', 'README.md', '--to', 'rst'],
                              stdout=subprocess.PIPE)
    readme = pandoc.communicate()[0]

except OSError:
    with open('README.md') as f:
        readme = f.read()

try:
    from Cython.Build import cythonize
    USE_CYTHON = True
except ImportError:
    USE_CYTHON = False

ext = '.pyx' if USE_CYTHON else '.c'

extensions = [Extension('harminv.charminv',
                        ["harminv/charminv" + ext],
                        libraries=['harminv'])]

if USE_CYTHON:
    extensions = cythonize(extensions)

setup(
    name='pharminv',
    version="0.2.1",
    description='Python interface to harminv',
    long_description=readme,
    packages=['harminv'],
    author="Aaron O'Leary",
    author_email='dev@aaren.me',
    license='GPLv3',
    url='http://github.com/aaren/harminv',
    install_requires=['numpy',],
    ext_modules=extensions
)
