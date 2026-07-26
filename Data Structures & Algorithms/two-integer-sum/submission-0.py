class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {val: index for index, val in enumerate(nums)}
        
        for i in range(len(nums)):
            difference = target - nums[i]
            if difference in hashmap and hashmap[difference] != i:
                return [i, hashmap[difference]]
        return []
