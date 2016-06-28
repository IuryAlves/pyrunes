# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

from .rune_map import runes
from .exceptions import RuneDoesNotExist


def to_rune(char, errors='strict'):
    if char == 'c':
        # c and k has the same rune
        char = 'k'
    return _get_key(runes, char, errors)


def to_latin(rune, errors='strict'):
    return _get_key(runes.inv, rune, errors)


def _get_key(dic, key, errors='strict'):
    try:
        return dic[key]
    except KeyError:
        if errors == 'strict':
            raise RuneDoesNotExist('The transliteration of "{key}" does not exist.'.format(key=key))
        return ''
