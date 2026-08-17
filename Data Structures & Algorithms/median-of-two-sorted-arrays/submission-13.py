class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        l = r = 0
        merged = []

        while l < n and r < m:
            if nums1[l] <= nums2[r]:
                merged.append(nums1[l])
                l += 1
            else:
                merged.append(nums2[r])
                r += 1
        
        merged += nums1[l:] or nums2[r:]

        print(merged)
        lenM = m + n
        if lenM % 2:
            median = float(merged[lenM // 2])
        else:
            leftMiddle = float(merged[lenM // 2])
            rightMiddle = float(merged[(lenM // 2) - 1])
            median = float((leftMiddle + rightMiddle) / 2)

        return median

