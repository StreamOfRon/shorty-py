from asyncio import to_thread as asyncify
from configparser import ConfigParser
import functools

from cache import NoOpCache
from models import HitCounter, ShortURL

def get_datastore(config: ConfigParser):
  if config['settings']['datastore'] == 'sql':
    datastore = SQLDatastore
  elif config['settings']['datastore'] == "detabase":
    datastore = DetaBaseDatastore
  else:
    raise RuntimeError(f"Unknown datastore type: {config['settings']['datastore']}")

  if config['settings']['cache'] == "none":
    cache = NoOpCache
  else:
    raise RuntimeError(f"Unknown cache type: {config['settings']['cache']}")

  class Datastore(datastore, cache):
    pass

  return Datastore(config)

def cache_wrapper(func):
  @functools.wraps(func)
  async def inner(self, cache_key):
    cache_value = await self.cache_get(cache_key)
    if cache_value is not None:
      return cache_value
    else:
      value = await func(cache_key)
      await self.cache_set(cache_key, value)
      return value
  return inner

class DatastoreInterface(object):
  def __init__(self, config: ConfigParser):
    raise NotImplementedError()

  def _init_datastore(self):
    raise NotImplementedError()

  async def get_url_for(self, shortened: str):
    raise NotImplementedError()

  async def add_url(self, data: ShortURL):
    raise NotImplementedError()

  async def update_url(self, data: ShortURL):
    raise NotImplementedError()

  async def delete_url(self, short_url):
    raise NotImplementedError()

  async def update_hits(self, short_url, hit_data: HitCounter):
    raise NotImplementedError()

class SQLDatastore(DatastoreInterface):
  def __init__(self, config: ConfigParser):
    pass

  @cache_wrapper
  async def get_url_for(self, shortened: str):
    pass

class DetaBaseDatastore(DatastoreInterface):
  def __init__(self, config: ConfigParser):
    pass
