class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()

        res = []
        for r in range(len(nums)):
            # New num
            while queue and nums[r] > nums[queue[-1]]:
                queue.pop()
            
            queue.append(r)
            
            if queue and queue[0] <= r - k:
                queue.popleft()
            
            if r + 1 >= k:
                res.append(nums[queue[0]])

        return res
