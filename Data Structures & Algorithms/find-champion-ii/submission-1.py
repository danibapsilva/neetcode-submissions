class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        has_incoming = [False] * n
        for _, v in edges:
            has_incoming[v] = True

        candidates = [i for i in range(n) if not has_incoming[i]]
        return candidates[0] if len(candidates) == 1 else -1