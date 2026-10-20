class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        first = second = third = False
        for triplet in triplets:
            ai, bi, ci = triplet
            x, y, z    = target
            if ai > x or bi > y or ci > z:
                continue
            
            if ai == x: first  = True
            if bi == y: second = True
            if ci == z: third  = True

            if first and second and third:
                return True
        return False
            
