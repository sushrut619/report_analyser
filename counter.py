"""Dictionary class which return integer 0 for uninitialized keys"""

class Counter(dict):
    """missing method is called when key is not present"""
    def __missing__(self, key):
        return 0
