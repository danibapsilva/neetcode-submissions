class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        for u, v, dist in roads:
            adj[u].append((v, dist))
            adj[v].append((u, dist))

        q, visited = deque([1]), set()
        res = float("inf")
        while q:
            node = q.popleft()
            if node in visited:
                continue
            
            visited.add(node)
            for nei, dist in adj[node]:
                res = min(res, dist)
                q.append(nei)
        
        return res
