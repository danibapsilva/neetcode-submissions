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

        # Build a frequency map of all cards.
        # For each unused card, find the lowest available number that could start
        # a straight by moving start backwards.
        # Then, from that start through the current num, greedily build every
        # possible consecutive group of size groupSize.
        # Decrement counts as cards are used, and if any required card is missing,
        # return False.
        # If all cards are successfully used, return True.