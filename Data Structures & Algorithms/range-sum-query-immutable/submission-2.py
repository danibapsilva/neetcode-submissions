class NumArray:

    def __init__(self, nums: List[int]):
        n = len(nums)
        self.prefix = [0] * (n + 1)

        for i in range(n):
            self.prefix[i + 1] = self.prefix[i] + nums[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right + 1] - self.prefix[left]


# range indx: 2-3
# nums: [1, 4, 5, 2, 9]
# pref: [0, 1, 5, 10, 12, 21]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)