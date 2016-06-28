#! /usr/bin/env python
# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

import sys
import unittest


def main():
    tests = unittest.TestLoader().discover("test", "*tests.py")
    result = unittest.TextTestRunner().run(tests)

    if not result.wasSuccessful():
        sys.exit(1)


if __name__ == '__main__':
    main()
