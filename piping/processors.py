
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


def pass_thru(iterable):
  for thing in iterable:
    yield thing


class discard(object):
  """
  This process just consumes everything in the upstream iterable.
  It's really only useful for Branches.
  """

  def __init__(self, iterable):
    self.iterable = iterable

  def __iter__(self):
    return self

  def next(self):
    for thing in self.iterable:
      pass
    raise StopIteration



class BranchRule(object):
  def __init__(self, condition, processor):
    self.condition = condition
    self.processor = processor


class Branch(object):
  def __init__(self, rules = None, otherwise = pass_thru):
    self.rules = rules or []
    self.otherwise = otherwise

  def __call__(self, iterable):
    for thing in iterable:
      for r in self.rules:
        if r.condition(thing):
          for outcome in r.processor([thing]):
            yield outcome
          break
      else:
        for outcome in self.otherwise([thing]):
          yield outcome

  def CASE(self, condition, processor):
    rules = self.rules[:]
    rules.insert(0, BranchRule(condition, processor))
    return Branch(rules, self.otherwise)

  def ELSE(self, processor):
    return Branch(self.rules, processor)


def Detour(condition, processor):
  """
  This is shorthand for creating a Branch w/ a single condition
  """
  return Branch([BranchRule(condition, processor)])

