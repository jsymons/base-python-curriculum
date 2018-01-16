class Calculator(object):
    def __init__(self):
        self.cache = {}

    def _find_cached_computation(self, operation, params):
        if operation not in self.cache:
            return None
        for prev_computations in self.cache[operation]:
            if prev_computations[:2] == params:
                return prev_computations[2]

    def _append_to_cache(self, operation, cached_value):
        self.cache.setdefault(operation, [])
        self.cache[operation].append(cached_value)

    def add(self, x, y):
        cached = self._find_cached_computation('add', (x, y))
        if not cached:
            cached = x + y
            self._append_to_cache('add', (x, y, cached))
        return cached

    def subtract(self, x, y):
        cached = self._find_cached_computation('subtract', (x, y))
        if not cached:
            cached = x - y
            self._append_to_cache('subtract', (x, y, cached))
        return cached
