class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1Set = set(nums1)

        res = []
        for num in nums2:
            if num in nums1Set:
                res.append(num)
                nums1Set.remove(num)
        return res