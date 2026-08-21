class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        boats = 0

        l, r = 0, len(people) - 1
        while l <= r:
            lWeight, rWeight = people[l], people[r]
            if lWeight + rWeight > limit:
                r -= 1
            else:
                l += 1
                r -= 1
            boats += 1
        
        return boats
        # [1, 2, 2, 3, 3] -> b1 [1, 2, 2, 3] -> b2 [1, 2, 2] ->
        # [5,1,4,2] -> [1,2,4,5] -> 