
from processors import Map, Tap, Select, Reject

class Stream(object):
  def __init__(self, iterable):
    self.iterable = iter(iterable)

  def __iter__(self):
    return self

  def next(self):
    return self.iterable.next()

  def pipe(self, processor):
    return Stream(processor(self.iterable))

  def map(self, fn):
    return self.pipe(Map(fn))

  def tap(self, fn):
    return self.pipe(Tap(fn))

  def select(self, fn):
    return self.pipe(Select(fn))

  def reject(self, fn):
    return self.pipe(Reject(fn))

  def each(self, func):
    for thing in self.iterable:
      func(thing)

