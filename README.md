
## This Module a translator between runes and they respective latin characters

### Usage

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

Not all latin caracter has a respective rune. The table below shows the available runes.

  |Latin char | Rune  |
  |-----------|:-----:|
  | a         |ᚨ      |
  | b         |ᛒ      |
  | c         |ᚲ      |
  | d         |ᛞ      |
  | e         |ᛖ      |
  | f         |ᚠ      |
  | g         |ᚷ      |
  | h         |ᚺᚻ     |
  | i         |ᛁ      |
  | l         |ᛚ      |
  | k         |ᚲ      |
  | m         |ᛗ      |
  | n         |ᚾ      |
  | o         |ᛟ      |
  | p         |ᛈ      |
  | r         |ᚱ      |
  | s         |ᛊᛋ     |
  | t         |ᛏ      |
  | u         |ᚢ      |
  | v         |ᚡ      |
  | w         |ᚹ      |
  | z         |ᛉ      |