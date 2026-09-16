class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.rank = [1] * n
    
    def find(self, node: int) -> int:
        curr = node
        while curr != self.parent[curr]:
            self.parent[curr] = self.parent[self.parent[curr]]
            curr = self.parent[curr]
        return curr
    
    def union(self, u: int, v: int) -> bool:
        pu, pv = self.find(u), self.find(v)
        if pu == pv:
            return False
        if self.rank[pv] > self.rank[pu]:
            pu, pv = pv, pu
        self.parent[pv] = pu
        self.rank[pu] += self.rank[pv]
        return True

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        dsu = DSU(n)

        for u, v in edges:
            if not dsu.union(u, v):
                return [u, v]
        return []