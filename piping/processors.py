
def Map(fn):
  def mapper(iterable):
    for thing in iterable:
      yield fn(thing)

  return mapper


def Tap(fn):
  def tapper(iterable):
    for thing in iterable:
      fn(thing)
      yield thing

  return tapper


def Select(fn):
  def selector(iterable):
    for thing in iterable:
      if fn(thing):
        yield thing

  return selector


def Reject(fn):
  def rejector(iterable):
    for thing in iterable:
      if not fn(thing):
        yield thing

  return rejector
