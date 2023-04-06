# Solving Problem with Python

The scripts in here are solving the following problems with python. See deatailed problem description below:

1. Design a Least Recently Used Cache
2.
3.
4.
5.
6.

## Problem 1 - Least Recently Used Cache

Design a data structure known as a **Least Recently Used (LRU) cache**. An LRU cache is a type of cache in which we remove the least recently used entry when the cache memory reaches its limit.

- In case of a `cache hit`, the `get()` operation should return the appropriate value.
- In case of a `cache miss`, the `get()` should return `-1`.
- While putting an element in the cache, the `set()` operation must insert the element. If the cache is full, the least recently used entry is removed first and then is the element inserted.

All operations must take `O(1)` time.

Usage:

```py
our_cache = LRU_Cache(5)

our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);


our_cache.get(1)       # returns 1
our_cache.get(2)       # returns 2
our_cache.get(9)      # returns -1
# because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

our_cache.get(3)      # returns -1
# because the cache reached it's capacity
# and 3 was the least recently used entry
```
