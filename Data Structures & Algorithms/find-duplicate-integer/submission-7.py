class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[nums[0]]
        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
        
        slow2 = 0
        while slow2 != slow:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow

        # This method uses each index/element in [1, n] inc. and identify a slow and
        # a fast pointer (which moves 2x fast), once the slow and the fast pointer
        # meet (the cycle is found), a mathematical proof identifies the fact that
        # the meeting point is inside a cycle formed by treating nums as a linked
        # list. Resetting a second pointer at index 0 and moving both pointers at
        # the same speed guarantees they meet exactly at the cycle entrance, which
        # corresponds to the duplicate number.
