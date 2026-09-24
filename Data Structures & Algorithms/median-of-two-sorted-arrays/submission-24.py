class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        A, B = nums1, nums2
        if n > m:
            A, B = B, A
            n, m = m, n
        
        total = n + m
        half = total // 2

        l, r = 0, n
        while True:
            i = (l + r) // 2
            j = half - i

            ALeft = A[i - 1] if i > 0 else float("-inf")
            ARight = A[i] if i < n else float("inf")
            BLeft = B[j - 1] if j > 0 else float("-inf")
            BRight = B[j] if j < m else float("inf")

            if ALeft <= BRight and BLeft <= ARight:
                if total % 2:
                    return min(ARight, BRight)
                return (max(ALeft, BLeft) + min(ARight, BRight)) / 2.0
            elif ALeft > BRight:
                r = i - 1
            else:
                l = i + 1