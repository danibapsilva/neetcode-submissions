class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # n = 5 -> [1, 2, 3, 4, 5]
        # times = [1, 2, 1] , [1, 4, 4]
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))
        
        dist = {node: float("inf") for node in range(1, n + 1)}
        def dfs(node: int, time: int) -> int:
            if time >= dist[node]:
                return

            dist[node] = time
            for nei, weight in adj[node]:
                dfs(nei, time + weight)
            
        
        dfs(k, 0)
        res = max(dist.values())
        return res if res != float("inf") else -1