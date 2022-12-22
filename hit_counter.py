from collections import defaultdict
from threading import Lock

import arrow


class HitCounter(object):
  def __init__(self):
    self._counts = defaultdict(0)
    self._timestamp = dict()
    self._lock = Lock()

  def add_hit(self, name):
    with self._lock:
      self._counts[name] += 1
      self._timestamp = arrow.utcnow()

  def flush_to_store(self, datastore):
    pass