class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        found = [-1] * n
        for u, v in edges:
            found[v] = v
        
        oneFound = False
        iFound = -1
        for i, num in enumerate(found):
            if i != num:
                iFound = i
                if oneFound:
                    return -1
                oneFound = True
        
        return iFound if oneFound else -1
