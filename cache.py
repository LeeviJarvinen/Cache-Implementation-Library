class Cache:
    def __init__(self, max_size: int, strategy = "rand"):

        if not isinstance(max_size, int):
            raise TypeError("type of max_size must be an integer")
        self.strategy = strategy
        self.max_size = max_size
        self.cache = {}

        if strategy == "lru":
            pass

    def set(self, key, value):
        if len(self.cache) + 1 > self.max_size and key not in self.cache:
            self._evict()
        self.cache[key] = value

    def get(self, key, default = None):
        return self.cache.get(key, default)

    def _evict(self):
        match self.strategy:
            case "rand":
                self._evict_random()
            case "lru":
                pass
            case "fifo":
                pass
            case _:
                pass

    def _evict_random(self):
        import random
        random_key = random.choice(list(self.cache.keys()))
        del self.cache[random_key]

    def print_cache(self):
        return self.cache

