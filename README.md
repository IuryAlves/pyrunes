[![Build Status](https://travis-ci.org/IuryAlves/pyrunes.svg?branch=master)](https://travis-ci.org/IuryAlves/pyrunes)
[![Coverage Status](https://coveralls.io/repos/github/IuryAlves/pyrunes/badge.svg?branch=master)](https://coveralls.io/github/IuryAlves/pyrunes?branch=master)

## This Module is a translator between runes and they respective latin characters

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

  Latin char | Rune  
  -----------|---------
   a         |ᚨ      
   b         |ᛒ      
   c         |ᚲ      
   d         |ᛞ      
   e         |ᛖ      
   f         |ᚠ
   g         |ᚷ      
   h         |ᚺᚻ     
   i         |ᛁ      
   l         |ᛚ      
   k         |ᚲ      
   m         |ᛗ      
   n         |ᚾ      
   o         |ᛟ      
   p         |ᛈ      
   r         |ᚱ      
   s         |ᛊᛋ     
   t         |ᛏ      
   u         |ᚢ      
   v         |ᚡ      
   w         |ᚹ      
   z         |ᛉ      

