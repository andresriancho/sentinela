#!/usr/bin/env python

from setuptools import setup, find_packages
from os.path import join, dirname


setup(
      name='sentinela',

      version='0.2',
      license = 'GNU General Public License v2 (GPLv2)',
      platforms='Linux',
      
      description=('Sentinela is a highly configurable operating system watchdog'
                   ' which can take actions based on pre-configured rules.'),
      long_description=open(join(dirname(__file__), 'README.md')).read(),
      
      author='Andres Riancho',
      author_email='andres.riancho@gmail.com',
      url='https://github.com/andresriancho/sentinela/',
      
      packages=find_packages(),
      include_package_data=True,
      install_requires=['python-daemon', 'psutils'],
      
      entry_points={
          'console_scripts':
              ['sentinela = sentinela.sentinela:main']
        },
      
      classifiers = [
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: System :: Monitoring'
        ],
      
     )