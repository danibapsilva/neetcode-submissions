class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2:
            return False
        
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
                if dp[target]:
                    return True
        
        return False

        # dp[j] represents if we can sum up to that number based on what we've seen
        # We check the total sum of the array, we can only make two valid subsets
        # if the total amount cant be divided equally/total amount is even, so if its
        # not, return False. We then define what we need to look to sum up to in a
        # singular group, we call this target, and make our dp array. 0 set to True
        # by default because we can always sum up to 0 by adding nothing. Then for
        # every number in arr, we see if we can add up to the sum from the target
        # to the number, meaning have we alredy calculated / seen a subset that sums
        # to this current number, if yes or if we have already seen this exact number
        # we set dp[j] to True. then at the end we see wether dp[target] was ever
        # found after checking all numbers and their prior possibility calculations