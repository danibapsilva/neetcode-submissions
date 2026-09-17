class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)

        l, r = 0, n - 1
        while l <= r:
            middle = l + (r - l) // 2

            if nums[middle] == target:
                return middle
            
            if nums[middle] >= nums[r]:
                if nums[l] <= target < nums[middle]:
                    r = middle - 1
                else:
                    l = middle + 1
            else:
                if nums[middle] < target <= nums[r]:
                    l = middle + 1
                else:
                    r = middle - 1

        return -1

        # we see which side of the array is sorted middle el > right el
        # if mid el > r el, then the left half is sorted, so we check if target is
        # in-between l el and mid el, if yes move r, otherwise its between
        # mid el and r el so move l
        # if mid el < r el, right half sorted and repeat steps above corrispondingly