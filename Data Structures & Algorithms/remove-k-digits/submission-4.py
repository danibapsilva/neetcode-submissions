class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        q = deque()
        for ch in num:
            while k > 0 and q and q[-1] > ch:
                k -= 1
                q.pop()
            q.append(ch)
        
        for _ in range(k):
            q.pop()
        
        while q and q[0] == '0':
            q.popleft()
        
        return ''.join(q) if q else '0'