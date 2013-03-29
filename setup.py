#!/usr/bin/env python

from distutils.core import setup

setup(name='sentinela',
      version='0.2',
      description=('Sentinela is a highly configurable operating system watchdog'
                   ' which can take actions based on pre-configured rules.'),
      author='Andres Riancho',
      author_email='andres.riancho@gmail.com',
      url='https://github.com/andresriancho/sentinela/',
      license = 'GPL',
      platforms='Linux',
      packages=['sentinela',],
      install_requires=['python-daemon', 'psutils'],
     )