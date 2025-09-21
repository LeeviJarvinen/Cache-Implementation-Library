# Cache Implementation

A flexible Python cache implementation supporting multiple eviction strategies with a pluggable architecture.

## Architecture

The cache system is built around a base class (`BaseCache`) that defines the core caching interface, with specific eviction strategies implemented as subclasses. This design allows for easy extension and consistent behavior across different cache types.

### Core Components

- **BaseCache**: Abstract base class providing the fundamental `get()` and `set()` operations
- **DoublyLinkedList**: Internal data structure used by LRU cache for efficient node manipulation
- **Strategy Pattern**: Each cache type implements specific hooks for access tracking and eviction decisions

## Available Cache Types

### LRU Cache (Least Recently Used)
Evicts the least recently accessed item when the cache reaches capacity. Uses a doubly-linked list for O(1) access pattern tracking and eviction.

```python
cache = LRUCache(max_size=100)
cache.set("key1", "value1")
cache.set("key2", "value2")
value = cache.get("key1")  # Moves key1 to front
```

### LFU Cache (Least Frequently Used)
Evicts the item with the lowest access frequency. Tracks access counts for each key and removes the least frequently accessed item during eviction.

```python
cache = LFUCache(max_size=100)
cache.set("key1", "value1")
cache.get("key1")  # Increases frequency
cache.get("key1")  # Increases frequency again
```

### FIFO Cache (First In, First Out)
Evicts items in the order they were added, regardless of access patterns. Maintains insertion order and removes the oldest item first.

```python
cache = FIFOCache(max_size=100)
cache.set("first", "value1")
cache.set("second", "value2")
# "first" will be evicted before "second"
```

### TTL Cache (Time To Live) (WIP)

Designed to support time-based expiration of cache entries, where items are evicted after a specified time period.

## Usage

...

## Features

- **Configurable Size**: Set maximum cache capacity during initialization
- **Type Safety**: Input validation for cache parameters
- **Consistent Interface**: All cache types use the same `get()` and `set()` methods
- **Extensible Design**: Easy to add new eviction strategies by extending `BaseCache`

## Error Handling

- Raises `TypeError` for invalid `max_size` types
- Raises `ValueError` for negative `max_size` values
- Raises `TypeError` for `None` keys during `set()` operations
