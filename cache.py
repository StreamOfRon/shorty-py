from configparser import ConfigParser

class CacheInterface(object):
  def __init__(self, config: ConfigParser):
    raise NotImplementedError()

  def _cache_init(self):
    raise NotImplementedError()

  async def cache_get(self, cache_key):
    raise NotImplementedError()

  async def cache_set(self, cache_key, cache_value):
    raise NotImplementedError()

  async def cache_remove(self, cache_key):
    raise NotImplementedError()

  async def cache_purge(self):
    raise NotImplementedError()


class NoOpCache(CacheInterface):
  def __init__(self):
    pass

  async def cache_get(self, cache_key):
    return None

  async def cache_set(self, cache_key, cache_value):
    pass

  async def cache_remove(self, cache_key):
    pass

  async def cache_purge(self):
    pass
