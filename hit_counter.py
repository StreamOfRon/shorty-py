from collections import defaultdict
from threading import Lock

import arrow


class HitCounter(object):
  """
  Buffer the hit count and last-accessed data for short URLs so that we're not 
  writing to the database with every read.  The intent is that flush_to_store 
  will be called every N seconds by a background task.
  """
  def __init__(self):
    self._counts = defaultdict(0)
    self._timestamp = dict()
    self._lock = Lock()

  def add_hit(self, name):
    with self._lock:
      self._counts[name] += 1
      self._timestamp[name] = arrow.utcnow()

  def flush_to_store(self, datastore):
    pass