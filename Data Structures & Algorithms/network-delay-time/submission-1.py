class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, w in times:
            adj[u].append((v, w))

        heap = [(0, k)]
        visited = set()
        time = 0
        while heap:
            weight, node = heapq.heappop(heap)
            if node in visited:
                continue
            
            time = weight
            visited.add(node)
            for nei, w in adj[node]:
                if nei not in visited:
                    heapq.heappush(heap, (weight + w, nei))
        return time if len(visited) == n else -1
