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
            while start <= num:
                while count[start]:
                    for i in range(groupSize):
                        if not count[start + i]:
                            return False
                        count[start + i] -= 1
                start += 1

        return True

        # We start by making a freq/count dict of all nums in hand
        # then iterate until found lowest bound number / start of potential straight
        # and then iterate backupwards incrementing by 1, the amount of groupSize
        # if we dont find that incremented number, we know greedily since we found the
        # lower bound that the num in hand would have to belong to, that hand is
        # not able to be fully completed so we return false, otherwise we make sure to
        # decrement count from the number just processed / added to the potential hand
        # dont forget to skip any number that has a count of 0 (already used in a hand)
        # if we make it through the entire loop, we can return True since no num missing