class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()

        res = []
        for r in range(len(nums)):
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            
            q.append(r)

            if q and r - k >= q[0]:
                q.popleft()

            if r + 1 >= k:
                res.append(nums[q[0]])
            
        
        return res