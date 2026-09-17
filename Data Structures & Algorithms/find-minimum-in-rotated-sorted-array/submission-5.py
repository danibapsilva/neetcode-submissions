class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums) - 1
        while l < r:
            middle = l + (r - l) // 2
            if nums[middle] > nums[r]:
                l = middle + 1
            else:
                r = middle
        
        return nums[r]

        # if middle element is greater than the right element, we know that the
        # left half of the arr is sorted and the right half has the smaller elements
        # so we move the left pointer passed middle pointer
        # otherwise we know the left half of the array is sorted and the smallest
        # element is from middle downwards so move the right pointer to middle