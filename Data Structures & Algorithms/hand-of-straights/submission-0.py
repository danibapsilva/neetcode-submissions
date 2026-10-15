class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize:
            return False

        count = defaultdict(int)
        for num in hand:
            count[num] += 1
        
        for num in hand:
            if not count[num]:
                continue
            start = num
            while count[start - 1]:
                start -= 1
            for i in range(groupSize):
                if not count[start + i]:
                    return False
                count[start + i] -= 1

        return True