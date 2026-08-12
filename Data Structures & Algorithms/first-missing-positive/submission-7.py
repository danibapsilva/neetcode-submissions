class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        indx = 0
        while indx < n:
            correct = nums[indx] - 1

            if (
                1 <= nums[indx] <= n - 1
                and nums[indx] != nums[correct]
            ):
                nums[indx], nums[correct] = nums[correct], nums[indx]
            else:
                indx += 1

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1