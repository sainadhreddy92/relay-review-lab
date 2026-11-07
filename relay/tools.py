from time import monotonic

class Tools:
    def __init__(self, fetch, clock=monotonic):
        self.fetch = fetch
        self.clock = clock
        self.cache = {}

    def lookup(self, catalog, item):
        now = self.clock()
        entry = self.cache.get(item)
        if entry is not None:
            saved_at, value = entry
            if now - saved_at < 10:
                return value

        value = self.fetch(catalog, item)
        self.cache[item] = (self.clock(), value)
        return value
