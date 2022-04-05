#!/usr/bin/env python3
# coding:utf-8
# Copyright (C) 2022 All rights reserved.
# FILENAME:  backends/memcached.py
# VERSION: 	 0.1.0
# CREATED: 	 2022-04-03 15:31
# AUTHOR: 	 Sitt Guruvanich <aekazitt@gmail.com>
# DESCRIPTION:
#
# HISTORY:
#*************************************************************
### Standard Packages ###
from dataclasses import dataclass
from typing import Optional, Tuple
### Third-Party Packages ###
from aiomcache import Client
### Local Modules ###
from fastapi_cachette.backends import Backend

@dataclass
class MemcachedBackend(Backend):
  mcache: Client
  expire: int = 0

  @classmethod
  async def init(cls, memcached_host: str, expire: Optional[int] = None) -> 'MemcachedBackend':
    return MemcachedBackend(Client(host=memcached_host), expire or cls.expire)

  async def fetch(self, key: str):
    return await self.mcache.get(key.encode())

  async def fetch_with_ttl(self, key: str) -> Tuple[int, str]:
    return 3600, await self.mcache.get(key.encode())

  async def put(self, key: str, value: str, expire: Optional[int] = None):
    return await self.mcache.set(key.encode(), value.encode(), exptime=expire or self.expire)

  async def clear(self, namespace: Optional[str] = None, key: Optional[str] = None):
    count: int = 0
    if namespace:
      raise NotImplementedError
    elif key:
      count += (0, 1)[await self.mcache.delete(key.encode())]      
    return count
