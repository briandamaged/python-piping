# piping #

It's like Ruby's enumerators and Node's streams.  But, in Python!

## Installation ##

```shell
pip install piping
```

## Examples ##

Here's a quick example:

```python
from __future__ import print_function

from piping import Stream, Select, Map

Stream(xrange(10))\
  .pipe(Select(lambda x: x % 2 == 0))\
  .pipe(Map(lambda x: x * x))\
  .each(print)
```

This can also be written as:

```python
from __future__ import print_function

from piping import Stream, Select, Map

Stream(xrange(10))\
  .pipe(
    Select(lambda x: x % 2 == 0),
    Map(lambda x: x * x)
  )\
  .each(print)
```

It can also be written as:

```python
from __future__ import print_function

from piping import Stream

Stream(xrange(10))\
  .select(lambda x: x % 2 == 0)\
  .map(lambda x: x * x)\
  .each(print)
```

You can find more examples in the ```/examples``` folder.

## Usage ##

This library just provides an API that makes it easy to compose ```processor``` functions.  A processor function is any function that conforms to the following interface:

```
f(iterable) -> iterator
```


