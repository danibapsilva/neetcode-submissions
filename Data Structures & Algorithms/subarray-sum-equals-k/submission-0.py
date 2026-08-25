class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSums = {0: 1}

        res = curr = 0
        for num in nums:
            curr += num
            need = curr - k

            res += prefixSums.get(need, 0)
            prefixSums[curr] = prefixSums.get(curr, 0) + 1

        return res
