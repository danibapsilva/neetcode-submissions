class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n

        # Reverse whole arr
        self.reverse(0, n - 1, nums)
        
        # Reverse first k elmnts
        self.reverse(0, k - 1, nums)
        
        # Reverse elmnts after k
        self.reverse(k, n - 1, nums)

    def reverse(self, l: int, r: int, nums: List[int]) -> None:
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1