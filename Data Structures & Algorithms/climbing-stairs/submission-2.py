class Solution:
    def climbStairs(self, n: int) -> int:
        one = two = 1
        for i in range(n - 2, -1, -1):
            temp = one
            one += two
            two = temp
        return one
        # as prior stated, start from 1, 1, then our `one pointer` will "shift left"
        # a.k.a, sum one pointer + two pointer, and the `two pointer` will
        # "shift right", a.k.a move to where one pointer was prior to shifts