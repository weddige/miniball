__author__ = 'Konstantin Weddige'
from distutils.core import setup, Extension


setup(
    name='Miniball',
    version='0.1',
    description='Smallest Enclosing Balls of Points',
    author='Bernd Gärtner, Konstantin Weddige',
    ext_modules=[
        Extension(
            'miniball',
            ['src/miniballmodule.cpp', ],
            language='c++',
        ),
    ],
)