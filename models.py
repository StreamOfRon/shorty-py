from datetime import datetime
from typing import Optional, Union

from pydantic import BaseModel

class ShortURL(BaseModel):
  short_url: str
  full_url: str

class HitCounter(BaseModel):
  hit_count: int
  last_hit: datetime
