class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        l, r = 1, max(piles)
        minS = r
        while l <= r:
            middle = l + (r - l) // 2
            time = 0
            for pile in piles:
                time += math.ceil(float(pile) / middle)
            
            if time > h:
                l = middle + 1
            else:
                minS = min(minS, middle)
                r = middle - 1
        return minS