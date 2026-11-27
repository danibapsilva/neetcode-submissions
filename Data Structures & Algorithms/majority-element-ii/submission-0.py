class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cand1 = cand2 = None
        cnt1 = cnt2 = 0
        for num in nums:
            if num == cand1: cnt1 += 1
            elif num == cand2: cnt2 += 1
            elif not cnt1: cand1, cnt1 = num, 1
            elif not cnt2: cand2, cnt2 = num, 1
            else: cnt1, cnt2 = cnt1 - 1, cnt2 - 1

        return [c for c in (cand1, cand2) if nums.count(c) > len(nums) // 3]