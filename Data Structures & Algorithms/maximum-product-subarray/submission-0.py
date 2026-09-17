class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]

        currMin = currMax = 1
        for num in nums:
            temp = currMax * num
            currMax = max(currMax * num, currMin * num, num)
            currMin = min(temp, currMin * num, num)

            res = max(res, currMax)
        return res


        # For every element iterate through, we want to use that element to find a
        # new current maximum and a new current mimimum, cuz the array has negatives
        # the current maximum/minimum can be found by comparing:
        # the current num, num * current minumum, and num * current maximum
        # then per each iteration, current maximum will succesfully find the max
        # value at that point in time, so we can update a local var like res