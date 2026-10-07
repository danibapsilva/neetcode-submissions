class Solution:
    def tribonacci(self, n: int) -> int:
        one, two, three = 0, 1, 1
        if n < 3:
            return 1 if n else 0
        
        for i in range(2, n):
            temp = one + two + three
            one = two
            two = three
            three = temp
        return three