
from __future__ import print_function

import __bootstrap

from piping import *

headlines = [
  "coffee drinkers are 10x smarter",
  "why people with teeth are more attractive",
  "can your hamster do this?",
  "is chocolate unhealthy, or un-unhealthy?"
]


class HeadlineContext(object):
  """
  This class allows us to track the tags that are associated
  with each headline.
  """
  def __init__(self, headline):
    self.headline = headline
    self.tags = []

  def __str__(self):
    return str({"headline": self.headline, "tags": self.tags})


def contains(*words):
  """
  Returns a function that checks for specific words
  """
  def checker(ctx):
    for w in words:
      if w in ctx.headline:
        return True
    return False

  return checker

def tag_as(*tags):
  """
  Returns a function that will apply the specified tags
  to a HeadlineContext
  """
  def tagger(ctx):
    for t in tags:
      ctx.tags.append(t)
  return tagger

def TagAs(*tags):
  """
  We'll use 'defer' to create a new processor that invokes the
  'tag_as' function for each HeadlineContext in the stream.
  """
  return defer.tap(tag_as(*tags))


Stream(headlines)\
  .map(HeadlineContext)\
  .detour(contains("coffee", "chocolate"), TagAs("caffeine"))\
  .detour(contains("dog", "hamster"), TagAs("animals"))\
  .detour(contains("health", "attractive"), TagAs("health"))\
  .detour(contains("attractive"), TagAs("beauty"))\
  .each(print)

