__author__ = "Konstantin Weddige"
from setuptools import setup, Extension
from wheel.bdist_wheel import bdist_wheel


# keep in sync with Py_LIMITED_API
MINIMAL_PYTHON_VERSION = (3, 6)

def _get_python_requires():
    return f">={'.'.join(str(_) for _ in MINIMAL_PYTHON_VERSION)}"

def _get_cpython_tag():
    return f"cp{''.join(str(_) for _ in MINIMAL_PYTHON_VERSION[:2])}"

with open("README.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()

class bdist_wheel_abi3(bdist_wheel):
    def get_tag(self):
        python, abi, plat = super().get_tag()

        if python.startswith("cp"):
            # on CPython, our wheels are abi3
            # and compatible down to MINIMAL_PYTHON_VERSION
            return _get_cpython_tag(), "abi3", plat

        return python, abi, plat
    
setup(
    name="MiniballCpp",
    version="0.2.3",
    description="Smallest Enclosing Balls of Points",
    long_description=long_description,
    author="Bernd Gärtner, Konstantin Weddige",
    url="https://github.com/weddige/miniball",
    packages=[
        "miniball",
    ],
    package_data={"miniball": ["py.typed"]},
    ext_modules=[
        Extension(
            "miniball.bindings",
            ["src/miniballmodule.cpp"],
            include_dirs=["src"],
            language="c++",
            py_limited_api=True,
        ),
    ],
    python_requires=_get_python_requires(),
    classifiers=[
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
    ],
    cmdclass={"bdist_wheel": bdist_wheel_abi3},
)
