#!/usr/bin/env python3

from distutils.core import setup
try:
    # Setuptools only needed for building the package
    import setuptools
except ImportError:
    pass

setup(name="visidata",
      version="0.35",
      description="a curses interface for exploring and arranging tabular data",
      long_description=open('README.md').read(),
      author="Saul Pwanson",
      author_email="vd@saul.pw",
      url="https://github.com/saulpw/visidata",
      download_url="https://raw.githubusercontent.com/saulpw/visidata/master/bin/vd",
      scripts=['bin/vd'],
      license="GPLv3",
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Environment :: Console',
          'Environment :: Console :: Curses',
          'Intended Audience :: Developers',
          'Intended Audience :: Science/Research',
          'Intended Audience :: System Administrators',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 3',
          'Topic :: Database :: Front-Ends',
          'Topic :: Scientific/Engineering',
          'Topic :: Office/Business :: Financial :: Spreadsheet',
          'Topic :: Scientific/Engineering :: Visualization',
          'Topic :: Utilities',
      ],
      keywords=("console tabular data spreadsheet viewer textpunk"
                "curses csv hdf5 h5 xlsx"),
      )
