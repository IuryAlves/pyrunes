# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

from .runic_alphabets import get_alphabet
from .exceptions import TransliterationDoesNotExist


def to_runes(chars, runic_alphabet='elder_futhark', errors='strict'):
    runic_alphabet = get_alphabet(runic_alphabet)
    for char in chars:
        yield _get_key(runic_alphabet, char, errors)


def to_rune(char, runic_alphabet='elder_futhark', errors='strict'):
    runic_alphabet = get_alphabet(runic_alphabet)
    return _get_key(runic_alphabet, char, errors)


def from_runes(runes, runic_alphabet='elder_futhark', errors='strict'):
    runic_alphabet = get_alphabet(runic_alphabet).inv
    for rune in runes:
        yield _get_key(runic_alphabet, rune, errors)


def from_rune(rune, runic_alphabet='elder_futhark', errors='strict'):
    runic_alphabet = get_alphabet(runic_alphabet)
    return _get_key(runic_alphabet.inv, rune, errors)


def _get_key(dic, key, errors='strict'):
    try:
        return dic[key]
    except KeyError:
        if errors == 'strict':
            raise TransliterationDoesNotExist('The transliteration of "{key}" does not exist.'.format(key=key))
        return ''
