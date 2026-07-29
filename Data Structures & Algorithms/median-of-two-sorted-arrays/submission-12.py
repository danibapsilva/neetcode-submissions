class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        m, n = len(nums1), len(nums2)

        i = j = 0
        merged = []

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                merged.append(nums1[i])
                i += 1
            else:
                merged.append(nums2[j])
                j += 1

        merged.extend(nums1[i:])
        merged.extend(nums2[j:])

        mid = (m + n) // 2

        if (m + n) % 2:
            return float(merged[mid])

        return (merged[mid] + merged[mid - 1]) / 2