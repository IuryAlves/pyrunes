# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)


from unittest import TestCase
from runes import to_rune


class RuneTranslatorTestCase(TestCase):

    def test_rune_f(self):
        self.assertEqual(to_rune('f'), '\u16a0')
