# bootstrap if we need to
try:
        import setuptools  # noqa
except ImportError:
        from ez_setup import use_setuptools
        use_setuptools()

from setuptools import setup, find_packages

classifiers = [ 'Development Status :: 4 - Beta'
              , 'Environment :: No Input/Output (Daemon)'
              , 'Intended Audience :: Developers'
              , 'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)'
              , 'Natural Language :: English'
              , 'Operating System :: OS Independent'
              , 'Programming Language :: Python :: 2.7'
              , 'Programming Language :: Python :: 3.5'
              , 'Programming Language :: Python :: Implementation :: CPython'
              , 'Topic :: Database :: Front-Ends'
              , 'Topic :: Software Development :: Libraries :: Python Modules'
              ]

setup( author = 'Paul Jimenez'
     , author_email = 'pj@place.org'
     , classifiers = classifiers
     , description = 'A QDB library for python'
     , name = 'pyqdb'
     , url = 'http://github.com/pjz/pyqdb'
     , packages = find_packages()
     , version = '0.4'
     , install_requires = [ 'requests' ]
     , extras_require = { 'tests': [ 'pytest', 'pytest-timeout', 'pytest-cov' ] },
      )

