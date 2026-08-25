class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = {}
        for task in tasks:
            freq[task] = freq.get(task, 0) + 1
        
        maxHeap = []
        for cnt in freq.values():
            heapq.heappush(maxHeap, -cnt)
        
        time = 0
        q = deque()
        while maxHeap or q:
            time += 1

            if not maxHeap:
                time = q[0][1]
            else:
                cnt = heapq.heappop(maxHeap) + 1
                if cnt:
                    q.append((cnt, time + n))
            
            if q and q[0][1] == time:
                cnt = q.popleft()[0]
                heapq.heappush(maxHeap, cnt)
            
        
        return time
            

