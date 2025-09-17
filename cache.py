class BaseCache:
    def __init__(self, max_size: int):
        if not isinstance(max_size, int):
            raise TypeError("max_size must be an integer")

        if max_size < 0:
            raise ValueError("max_size cannot be negative")

        self.max_size = max_size
        self.cache = {}
        self._setup_strategy()


    def get(self, key):
        if key in self.cache:
            self._on_access(key)
            return self.cache[key]

        return None


    def set(self, key, value):
        if len(self.cache) > self.max_size and key not in self.cache:
            key_to_evict = self._get_eviction_key()
            del self.cache[key_to_evict]

        if key not in self.cache:
            self._on_new_key(key)

        if key in self.cache:
            self._on_access(key)

        self.cache[key] = value


    def _setup_strategy(self): pass
    def _on_access(self, key): pass
    def _on_new_key(self, key): pass
    def _get_eviction_key(self): pass
    #def _on_eviction(self, key): pass

class LRUCache(BaseCache):
    def _setup_strategy(self):
        self.order = []    

    def _on_access(self, key):
        self.order.remove(key)
        self.order.insert(0, key)

    def _on_new_key(self, key):
        self.order.insert(0, key)

    def _get_eviction_key(self):
        return self.order.pop()

class LFUCache(BaseCache):
    def _setup_strategy(self):
        self.frequency = {}

    def _on_access(self, key):
        self.frequency[key] += 1

    def _on_new_key(self, key):
        self.frequency[key] = 0

    def _get_eviction_key(self):
        least_frequent = min(self.frequency, key=self.frequency.get)
        self.frequency.pop(least_frequent)
        return least_frequent 

class FIFOCache(BaseCache):
    def _setup_strategy(self):
        self.insertion_order = []

    def _on_access(self, key):
        pass

    def _on_new_key(self, key):
        self.insertion_order.append(key)

    def _get_eviction_key(self):
        return self.insertion_order.pop(0)
