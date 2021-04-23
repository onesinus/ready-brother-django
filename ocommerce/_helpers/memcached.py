from django.core.cache import caches, InvalidCacheBackendError


class MemcachedHelper:
    def __init__(self):
        try:
            self.cache = caches['default']
        except (
                InvalidCacheBackendError,
                Exception
        ) as e:
            self.cache = False

    def set_value(self, key, value, timeout=86400):
        if self.cache:
            self.cache.set(key, value, timeout)

    def get_value(self, key):
        if self.cache:
            return self.cache.get(key)
        
    def delete_value(self, key):
        if self.cache:
            self.cache.delete(key)
