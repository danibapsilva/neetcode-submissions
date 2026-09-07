class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        adj = [[] for _ in range(n + 1)]
        
        def dfs(node: int, parent: int) -> bool:
            if visited[node]:
                return True

            visited[node] = True
            for nei in adj[node]:
                if nei == parent:
                    continue
                if dfs(nei, node):
                    return True
            return False
        
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            visited = [False] * (n + 1)

            if dfs(u, -1):
                return [u, v]
        return []