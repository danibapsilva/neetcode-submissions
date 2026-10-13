class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n = len(nums1)
        nums1Indx = {num:indx for indx, num in enumerate(nums1)}

        res = [-1] * n
        stack = []
        for num in nums2:
            while stack and num > stack[-1]:
                val = stack.pop()
                indx = nums1Indx[val]
                res[indx] = num
            if num in nums1Indx:
                stack.append(num)
        return res
