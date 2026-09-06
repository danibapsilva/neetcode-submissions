class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        total = set()

        def dfs(node: int, parent: int) -> bool:
            if node in visited:
                return False
            
            visited.add(node)
            total.add(node)
            for nei in adj[node]:
                if nei == parent:
                    continue
                
                if not dfs(nei, node):
                    return False                

            visited.remove(node)
            return True
        
        return dfs(0, -1) and len(total) == n