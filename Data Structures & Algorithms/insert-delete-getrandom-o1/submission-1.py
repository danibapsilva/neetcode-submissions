class RandomizedSet:

    def __init__(self):
        self.nums = []
        self.mp = {}

    def insert(self, val: int) -> bool:
        if val in self.mp:
            return False
        self.mp[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.mp:
            return False

        indx = self.mp[val]
        last = self.nums[-1]
        self.nums[indx], self.nums[-1] = self.nums[-1], self.nums[indx]
        self.mp[last] = indx
        self.nums.pop()
        del self.mp[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()