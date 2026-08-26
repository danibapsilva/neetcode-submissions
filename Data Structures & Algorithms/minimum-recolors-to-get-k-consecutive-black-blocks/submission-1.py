class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        l = whites = 0
        minOp = float("inf")
        for r in range(len(blocks)):
            if blocks[r] == 'W':
                whites += 1
            if r >= k - 1:
                minOp = min(minOp, whites)
                if blocks[l] == 'W':
                    whites -= 1
                l += 1
        
        return minOp

