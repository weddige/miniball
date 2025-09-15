__author__ = "Konstantin Weddige"
import sysconfig
from setuptools import setup, Extension


MINIMAL_PYTHON_VERSION = major, minor = (3, 6)

# build with Py_LIMITED_API unless in freethreading build (which does not currently
# support the limited API in py313t)
USE_PY_LIMITED_API = not sysconfig.get_config_var("Py_GIL_DISABLED")
define_macros = []

if USE_PY_LIMITED_API:
    define_macros.append(("Py_LIMITED_API", f"0x{major:02X}{minor:02X}0000"))
    options = {"bdist_wheel": {"py_limited_api": f"cp{major}{minor}"}}
else:
    options = {}

with open("README.rst", "r", encoding="utf-8") as fh:
    long_description = fh.read()

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
            define_macros=define_macros,
            py_limited_api=USE_PY_LIMITED_API,
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
    options=options,
)
