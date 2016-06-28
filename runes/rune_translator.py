# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

from .rune_map import ascii_to_rune


def to_rune(chars):
    result = ''
    for char in chars:
        result += ascii_to_rune.get(char, '')
    return result
