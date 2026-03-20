class RandomizedSet:

    def __init__(self):
        self.set1 = set()

    def insert(self, val: int) -> bool:
        if val not in self.set1:
            self.set1.add(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val not in self.set1:
            return False
        else:
            self.set1.remove(val)
            return True

    def getRandom(self) -> int:
        return random.choice((list(self.set1)))


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()