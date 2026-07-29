class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)

        res = []
        l = r = 0
        while l < m and r < n:
            if nums1[l] <= nums2[r]:
                res.append(nums1[l])
                l += 1
            else:
                res.append(nums2[r])
                r += 1
        
        res.extend(nums1[l:])
        res.extend(nums2[r:])
        
        median = (
            float(res[(n + m) // 2]) if (n + m) % 2 != 0
            else (float(res[(n + m) // 2]) + float(res[((n + m) // 2) - 1])) / 2
        )
        return median