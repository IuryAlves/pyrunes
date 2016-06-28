# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

from .rune_map import runes


def to_rune(char):
    if char == 'c':
        # c and k has the same rune
        return runes.get('k', '')
    return runes.get(char, '')


def to_latin(rune):
    return runes.inv.get(rune, '')
