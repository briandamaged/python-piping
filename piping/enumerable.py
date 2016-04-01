
from .processors import Map, Tap, Select, Reject, Branch

class Enumerable(object):
  """
  Stream and Defer classes both support these methods.
  So, why not extract them into a Mixin?
  """

  def map(self, fn):
    return self.pipe(Map(fn))

  def tap(self, fn):
    return self.pipe(Tap(fn))

  def select(self, fn):
    return self.pipe(Select(fn))

  def reject(self, fn):
    return self.pipe(Reject(fn))

  def detour(self, condition, processor):
    return self.pipe(Branch().CASE(condition, processor))
