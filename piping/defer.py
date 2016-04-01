
from .enumerable import Enumerable
from .stream import Stream

class Defer(Enumerable):
  def pipe(self, *processors):
    return reduce(lambda d, p: DeferMore(d, p), processors, self)

  def __call__(self, iterable):
    return Stream(iterable)


class DeferMore(Defer):
  def __init__(self, previous, processor):
    self.previous = previous
    self.processor = processor

  def __call__(self, iterable):
    return self.previous(iterable).pipe(self.processor)

defer = Defer()

def pipe(*processors):
  return defer.pipe(*processors)
