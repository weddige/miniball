__author__ = "Konstantin Weddige"
from setuptools import setup, Extension

with open("README.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="MiniballCpp",
    version="0.2.2",
    description="Smallest Enclosing Balls of Points",
    long_description=long_description,
    author="Bernd Gärtner, Konstantin Weddige",
    url="https://github.com/weddige/miniball",
    packages=["miniball",],
    package_data={"miniball": ["py.typed"]},
    ext_modules=[
        Extension(
            "miniball.bindings",
            ["src/miniballmodule.cpp"],
            include_dirs=["src"],
            language="c++",
        ),
    ],
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
    ],
)
