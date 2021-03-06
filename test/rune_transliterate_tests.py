# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)


from unittest import TestCase
from runes import (
    to_rune,
    from_rune, from_runes,
    to_runes,
    TransliterationDoesNotExist
)


class FromRunesTestCase(TestCase):

    def test_from_runes(self):
        gen = from_runes('ᚲᚺ')

        self.assertEqual(next(gen), 'k')
        self.assertEqual(next(gen), 'h')

        with self.assertRaises(StopIteration):
            next(gen)


class ToRunesTestCase(TestCase):

    def test_to_runes(self):
        gen = to_runes('vu')

        self.assertEqual(next(gen), '\u16a1')
        self.assertEqual(next(gen), '\u16A2')

        with self.assertRaises(StopIteration):
            next(gen)


class FromRuneTestCase(TestCase):

    def test_from_rune_a(self):
        self.assertEqual(from_rune('\u16A8'), 'a')

    def test_from_rune_r(self):
        self.assertEqual(from_rune('ᚱ'), 'r')


class ToRuneTestCase(TestCase):

    def test_rune_a_strict(self):
        with self.assertRaises(TransliterationDoesNotExist):
            to_rune('q')

    def test_rune_f(self):
        self.assertEqual(to_rune('f'), '\u16a0')

    def test_rune_v(self):
        self.assertEqual(to_rune('v'), '\u16a1')

    def test_rune_u(self):
        self.assertEqual(to_rune('u'), '\u16A2')

    def test_rune_a(self):
        self.assertEqual(to_rune('a'), '\u16A8')

    def test_rune_r(self):
        self.assertEqual(to_rune('r'), '\u16b1')

    def test_rune_k(self):
        self.assertEqual(to_rune('k'), '\u16B2')

    def test_rune_h(self):
        self.assertEqual(to_rune('h'), '\u16BA')

    def test_rune_w(self):
        self.assertEqual(to_rune('w'), '\u16B9')

    def test_rune_n(self):
        self.assertEqual(to_rune('n'), '\u16BE')

    def test_rune_i(self):
        self.assertEqual(to_rune('i'), '\u16C1')

    def test_rune_p(self):
        self.assertEqual(to_rune('p'), '\u16C8')

    def test_rune_z(self):
        self.assertEqual(to_rune('z'), '\u16C9')

    def test_rune_s(self):
        self.assertEqual(to_rune('s'), '\u16CA')

    def test_rune_t(self):
        self.assertEqual(to_rune('t'), '\u16CF')

    def test_rune_b(self):
        self.assertEqual(to_rune('b'), '\u16D2')

    def test_rune_e(self):
        self.assertEqual(to_rune('e'), '\u16D6')

    def test_rune_m(self):
        self.assertEqual(to_rune('m'), '\u16D7')

    def test_rune_l(self):
        self.assertEqual(to_rune('l'), '\u16DA')

    def test_rune_o(self):
        self.assertEqual(to_rune('o'), '\u16DF')

    def test_rune_d(self):
        self.assertEqual(to_rune('d'), '\u16DE')
