#!/usr/bin/env python3
""" 0. Writing strings to Redis """

import redis
import uuid
from typing import Union


class Cache:
    """
    A simple caching class using Redis as the backend.

    This class provides a way to store data of
    various types in a Redis database,
    using a randomly generated UUID as the key.
    """

    def __init__(self) -> None:
        """
        Initialize the Cache class.

        This method creates a Redis object
        and flushes the Redis database.
        """
        self._redis: redis.Redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Store the given data in the Redis database.

        This method generates a random UUID to use as the key
        and stores the provided
        data under this key in the Redis database.

        Parameters:
        data (Union[str, bytes, int, float]): The data to be stored.

        Returns:
        str: The key under which the data is stored.
        """
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
