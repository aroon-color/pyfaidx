import sys
from io import open

from setuptools import setup

install_requires = ["six", "setuptools >= 0.7"]
if sys.version_info[0] == 2 and sys.version_info[1] == 6:
    install_requires.extend(["ordereddict", "argparse"])

setup(
    name="pyfaidx",
    provides="pyfaidx",
    author="Matthew Shirley",
    author_email="mdshw5@gmail.com",
    url="http://mattshirley.com",
    description="pyfaidx: efficient pythonic random " "access to fasta subsequences",
    long_description=open("README.rst", encoding="utf-8").read(),
    license="BSD",
    packages=["pyfaidx"],
    install_requires=install_requires,
    python_requires=">=3.7",
    use_scm_version={"local_scheme": "no-local-version"},
    setup_requires=["setuptools_scm"],
    entry_points={"console_scripts": ["faidx = pyfaidx.cli:main"]},
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: BSD License",
        "Environment :: Console",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Operating System :: Unix",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
    ],
)
