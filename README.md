[![Build Status](https://travis-ci.org/IuryAlves/pyrunes.svg?branch=master)](https://travis-ci.org/IuryAlves/pyrunes)
[![Coverage Status](https://coveralls.io/repos/github/IuryAlves/pyrunes/badge.svg?branch=master)](https://coveralls.io/github/IuryAlves/pyrunes?branch=master)



## PyRunes

[![rune snake](rune_snake.jpg)](rune_snake.jpg)

PyRunes is a transliterator between runes and latin chars. It uses de default runic codes present in [unicode](https://en.wikipedia.org/wiki/Runic_(Unicode_block)).

### Usage

#### To rune

```python
>>> from runes import to_rune
>>> print(to_rune('a'))
ᚠ
```

Without the `print`, it will return the rune unicode code.

```python
>>> to_rune('a')
u'\u16a8'
```

#### From rune

```python
>>> from runes import to_latin
>>> to_latin(u'ᚱ')
'r'
```

#### Exceptions

The default behavior is to raise an exception if the rune does not exist.

```python
>>> to_rune("q")
 ...
 runes.exceptions.RuneDoesNotExist: The transliteration of "j" does not exist.
```

You can set the `errors` argument  to 'ignore', so instead of raising a exception, it will return an empty string.

```python
>>> to_rune("q", errors='ignore')
u''
```

#### Notes

Not all latin caracter has a respective rune. The table below shows the available runes.

     Rune    | transliteration
  -----------|----------------
   ᚨ         |   a
   ᚦ         |   þ
   ᛒ         |   b   
   ᚲ         |   c   
   ᛞ         |   d   
   ᛖ         |   e  
   ᚠ         |   f
   ᚷ         |   g   
   ᚺ         |   h  
   ᛁ         |   i
   ᛇ         |   ï 
   ᛃ         |   j  
   ᛚ         |   l   
   ᚲ         |   k   
   ᛗ         |   m   
   ᚾ         |   n
   ᛜ         |   ng
   ᛟ         |   o 
   ᛈ         |   p
   ᚱ         |   r
   ᛋ         |   s
   ᛏ         |   t
   ᚢ         |   u
   ᚹ         |   w
   ᛉ         |   z

