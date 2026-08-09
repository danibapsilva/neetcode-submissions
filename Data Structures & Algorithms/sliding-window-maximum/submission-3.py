class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []

        queue = deque()
        for r in range(len(nums)):
            while queue and nums[r] > nums[queue[-1]]:
                queue.pop()
            
            queue.append(r)

            if queue and r - k >= queue[0]:
                queue.popleft()
            
            if r + 1 >= k:
                res.append(nums[queue[0]])
        
        return res