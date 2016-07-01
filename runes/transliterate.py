# coding: utf-8

from __future__ import (
    absolute_import,
    unicode_literals
)

from .runic_alphabets import get_alphabet
from .exceptions import TransliterationDoesNotExist


def to_runes(chars, runic_alphabet='elder_futhark', errors='strict'):
    runes = get_alphabet(runic_alphabet)
    for char in chars:
        yield _get_key(runes, char, errors)


def to_rune(char, runic_alphabet='elder_futhark', errors='strict'):
    runes = get_alphabet(runic_alphabet)
    return _get_key(runes, char, errors)


def to_latin(rune, runic_alphabet='elder_futhark', errors='strict'):
    runes = get_alphabet(runic_alphabet)
    return _get_key(runes.inv, rune, errors)


def _get_key(dic, key, errors='strict'):
    try:
        return dic[key]
    except KeyError:
        if errors == 'strict':
            raise TransliterationDoesNotExist('The transliteration of "{key}" does not exist.'.format(key=key))
        return ''
