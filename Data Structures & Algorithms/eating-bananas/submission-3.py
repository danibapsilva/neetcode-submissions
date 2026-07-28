class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            middle = l + (r - l) // 2
            currH = 0
            for pile in piles:
                currH += math.ceil(float(pile) / middle)
            if currH <= h:
                res = middle
                r = middle - 1
            else:
                l = middle + 1
        
        return res

