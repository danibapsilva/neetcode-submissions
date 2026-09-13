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
        self.rank[pu] += self.rank[pv]
        self.parent[pv] = pu
        return True 

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        components, dsu = n, DSU(n)
        for u, v in edges:
            if dsu.union(u, v):
                components -= 1
        return components