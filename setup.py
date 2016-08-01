# bootstrap if we need to
try:
        import setuptools  # noqa
except ImportError:
        from ez_setup import use_setuptools
        use_setuptools()

from setuptools import setup, find_packages

classifiers = [ 'Development Status :: 5 - Production/Stable'
              , 'Environment :: Console'
              , 'Intended Audience :: Developers'
              , 'Intended Audience :: End Users/Desktop'
              , 'Intended Audience :: System Administrators'
              , 'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)'
              , 'Natural Language :: English'
              , 'Operating System :: MacOS :: MacOS X'
              , 'Operating System :: Microsoft :: Windows'
              , 'Operating System :: POSIX'
              , 'Programming Language :: Python :: 2.7'
              , 'Programming Language :: Python :: Implementation :: CPython'
              , 'Topic :: Communications :: Email :: Email Clients (MUA)'
              ]

setup( author = 'Paul Jimenez'
     , author_email = 'pj@place.org'
     , classifiers = classifiers
     , description = 'A QDB library for python'
     , name = 'pyqdb'
     , url = 'http://github.com/pjz/pyqdb'
     , packages = find_packages()
     , version = '0.1'
     , install_requires = [ 'requests' ]
     , extras_require = { 'tests': [ 'pytest', 'pytest-timeout', 'pytest-cov' ] },
      )

