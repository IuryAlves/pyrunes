# Documentation

## Functions 

* [to_rune](#to_rune) returns the rune transliteration of one latin character
* [to_latin](#to_latin) returns the latin transliteration of one runic character
* [to_runes](#to_runes) yields the rune transliteration of latin characters.


#### to_rune
<a name="to_rune"></a>

`to_rune(char, runic_alphabet='elder_futhark', errors='strict')`

Returns the rune transliteration of one latin character.

```python
>>> from runes import to_rune
>>> to_rune('a')
u'\u16a8'
```

`runic_alphabet` 

is the runic alphabet to use, currently only [elder_futhark](https://en.wikipedia.org/wiki/Elder_Futhark) is supported. Defaults to `elder_futhark`.

`errors` 

* if is set to `strict`, it will raise TransliterationDoesNotExist if the transliteration does not exist.
* if is set to `ignore`, it will return a empty string if the transliteration does not exist.


#### to_latin
<a name="to_latin"></a>

`to_latin(rune, runic_alphabet='elder_futhark', errors='strict')`

Returns the latin transliteration of one runic character.

```python
>>> from runes import to_latin
>>> to_latin('ᚱ')
'r'
```

`runic_alphabet` 

is the runic alphabet to use, currently only [elder_futhark](https://en.wikipedia.org/wiki/Elder_Futhark) is supported. Defaults to `elder_futhark`.

`errors` 

* if is set to `strict`, it will raise TransliterationDoesNotExist if the transliteration does not exist.
* if is set to `ignore`, it will return a empty string if the transliteration does not exist.


#### to_runes
<a name="to_runes"></a>

`to_runes(chars, runic_alphabet='elder_futhark', errors='strict')`

Returns a generator which have the transliteration of latin characters.

```python
>>> from runes import to_runes
>>> rune_gen = to_runes("ab")
>>> rune_gen
<generator object to_runes at 0x7f5b22aa8780>
>>> print(next(rune_gen))
ᚨ
>>> print(next(rune_gen))
ᛒ
>>> print(next(rune_gen))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
StopIteration
```

`runic_alphabet` 

is the runic alphabet to use, currently only [elder_futhark](https://en.wikipedia.org/wiki/Elder_Futhark) is supported. Defaults to `elder_futhark`.

`errors` 

* if is set to `strict`, it will raise TransliterationDoesNotExist if the transliteration does not exist.
* if is set to `ignore`, it will return a empty string if the transliteration does not exist.


## Exceptions

* [TransliterationDoesNotExist](#transliteration_does_not_exist)

#### TransliterationDoesNotExist
<a name="transliteration_does_not_exist"></a>

Raised when a rune or latin character does not have a transliteration.
