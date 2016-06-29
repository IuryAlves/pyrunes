# coding: utf-8


from __future__ import (
    absolute_import,
    unicode_literals
)

from bidict import bidict


elder_futhark = bidict(
    f="\u16A0",
    v='\u16A1',
    u="\u16A2",
    a="\u16A8",
    r="\u16B1",
    k="\u16B2",
    g="\u16B7",
    w="\u16B9",
    h="\u16BA",
    n="\u16BE",
    i="\u16C1",
    p="\u16C8",
    j="\u16C3",
    z="\u16C9",
    s="\u16CA",
    t="\u16CF",
    b="\u16D2",
    ng="\u16DC",
    e="\u16D6",
    m="\u16D7",
    l="\u16DA",
    o="\u16DF",
    d="\u16DE"
)

elder_futhark.update({"\xef": "\u16c7", "\xfe": "\u16A6"})


def get_alphabet(runic_alphabet):
    runic_alphabets = {
        'elder_futhark': elder_futhark
    }
    return runic_alphabets.get(runic_alphabet)
