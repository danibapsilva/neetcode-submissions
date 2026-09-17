class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixSums = defaultdict(int)
        prefixSums[0] = 1

        res = curr = 0
        for num in nums:
            curr += num
            need = curr - k
            res += prefixSums[need]

            prefixSums[curr] += 1
        return res
            