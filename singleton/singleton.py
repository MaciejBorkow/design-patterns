# one instance
class SingletonClass1:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance


class SingletonClass2:
    _instance = None

    @classmethod
    def get_instance(cls):
        if not cls._instance:
            cls._instance = cls()
        return cls._instance


obj1 = SingletonClass1()
obj2 = SingletonClass1()
print(f"SingletoneClass1 two instances are the same object: {obj1 is obj2}")


obj1 = SingletonClass2.get_instance()
obj2 = SingletonClass2.get_instance()
print(f"SingletoneClass2 two instances are the same object: {obj1 is obj2}")

from singleton_pythonic import my_singleton as obj1
from singleton_pythonic import my_singleton as obj2
print(f"SingletoneClass2 two instances are the same object: {obj1 is obj2}")
