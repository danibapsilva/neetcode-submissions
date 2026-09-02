class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()

        res = []
        for r, num in enumerate(nums):
            while q and num > nums[q[-1]]:
                q.pop()
            q.append(r)
            if q and q[0] <= r - k:
                q.popleft()
            
            if r >= k - 1:
                res.append(nums[q[0]])

        return res