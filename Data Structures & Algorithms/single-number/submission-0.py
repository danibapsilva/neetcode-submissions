class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res = num ^ res
        return res

        # If all numbers other than the answer, are present twice (even # of times)
        # they will XOR an even amount, meaning they will equal 0, so the only number
        # that is only present once, will change zero to flip on the bits of itself
        # leaving the final answer, res, to be the answer number