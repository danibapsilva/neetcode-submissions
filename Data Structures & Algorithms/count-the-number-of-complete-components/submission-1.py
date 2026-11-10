class DSU:
    def __init__(self, n: int) -> None:
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
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        # (k(k - 1)) / 2
        dsu = DSU(n)
        for u, v in edges:
            dsu.union(u, v)
        
        edgeCount = [0] * n
        for u, v in edges:
            root = dsu.find(u)
            edgeCount[root] += 1
        
        res = 0
        for i in range(n):
            if dsu.parent[i] == i:
                if edgeCount[i] == (dsu.rank[i] * (dsu.rank[i] - 1)) // 2:
                    res += 1
        return res
