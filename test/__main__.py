# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)


if __name__ == '__main__':
    import sys
    import unittest

    from runes import rune_translator

    tests = unittest.TestLoader().discover("test", "*tests.py")
    result = unittest.TextTestRunner().run(tests)

    if not result.wasSuccessful():
        sys.exit(1)
