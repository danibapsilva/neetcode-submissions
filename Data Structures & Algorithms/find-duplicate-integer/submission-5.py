class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # for num in nums:
        #     indx = abs(num)
        #     if nums[indx] < 0:
        #         return abs(num)
            
        #     nums[indx] *= -1

        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        slow2 = 0
        while slow2 != slow:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow