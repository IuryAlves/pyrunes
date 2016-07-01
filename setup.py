#!/usr/bin/env python

import re

from distutils.core import setup


def parse_requirements(requirements_file):
    requirements = []
    with open(requirements_file) as file_:
        for line in file_:
            if re.match(r'^\w+==[0-9.]+$', line):
                requirements.append(line)
    return requirements


setup(name='pyrunes',
      version='0.1',
      description='Transliterate latin characters into runes',
      author='Iury Alves',
      author_email='iuryalves20@gmail.com',
      packages=['runes'],
      install_requires=parse_requirements("requirements/base.txt")
     )
