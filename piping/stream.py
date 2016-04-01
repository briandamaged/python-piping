
from .enumerable import Enumerable

class Stream(Enumerable):
  def __init__(self, iterable):
    self.iterable = iter(iterable)

  def __iter__(self):
    return self

  def next(self):
    return self.iterable.next()

  def pipe(self, *processors):
    processor = reduce(lambda i, p: p(i), processors, self.iterable)
    return Stream(processor)

  def each(self, func):
    for thing in self.iterable:
      func(thing)

