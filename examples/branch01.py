
from __future__ import print_function

import __bootstrap

from piping import *

Stream(xrange(10))\
  .pipe(
    Branch()
      .CASE(lambda x: x < 3, Map(lambda x: [x, "too small"]))
      .CASE(lambda x: x > 7, Map(lambda x: [x, "TOO BIG"]))
      .ELSE(Map(lambda x: [x, "Just Right :)"]))
  )\
  .each(print)
