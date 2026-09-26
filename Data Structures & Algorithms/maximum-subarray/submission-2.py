class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxS, curr = nums[0], 0
        for num in nums:
            if curr < 0:
                curr = 0
            curr += num
            maxS = max(maxS, curr)
        return maxS

        # We can take a greedy approach here and notice that if we have a current
        # subarray count that is less than 0, then we want to reset the current count
        # or in other words we want to reset the count/ignore the curr numbers since
        # 0 would already be greater than anything we added (the negatives). so for
        # each number we add it to the current amount and calculate the local max
        # based on this current, then next iteration we check if the current count
        # is less than 0 and can be reset/restarted to view a new possible candidate
        # subarray and start counting from there.