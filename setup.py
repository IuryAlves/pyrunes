#!/usr/bin/env python

from setuptools import setup


setup(name='pyrunes',
      version='0.2.0',
      url="https://github.com/IuryAlves/pyrunes",
      description='Transliterate latin characters into runes',
      author='Iury Alves',
      author_email='iuryalves20@gmail.com',
      packages=['runes'],
      install_requires=["bidict==0.1.5"]
      )
