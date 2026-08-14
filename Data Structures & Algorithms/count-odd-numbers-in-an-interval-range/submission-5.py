class Solution:
    def countOdds(self, low: int, high: int) -> int:
        diff = high - low
        count = diff // 2
        if low % 2 and high % 2:
            count -= 1
            count += 2
        elif high % 2:
            count += 1
        elif low % 2:
            count += 1
        
        return count
        