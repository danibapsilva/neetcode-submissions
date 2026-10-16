class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)

        dp = {}
        def dfs(l: int, r: int) -> int:
            if l > r:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]
            
            dp[(l, r)] = 0
            for i in range(l, r + 1):
                coins = nums[l - 1] * nums[i] * nums[r + 1]
                coins += dfs(l, i - 1) + dfs(i + 1, r)
                dp[(l, r)] = max(dp[(l, r)], coins)
            return dp[(l, r)]
        
        return dfs(1, n - 2)

        # Instead of rebuilding a new array when we decide which balloon to pop, we find
        # which balloon to pop LAST because then the subproblems appear and we can use a
        # cache. We use two pointers, l and r, because we dont want to make copies of
        # the input array. After we decide which balloon we want to pop last (in loop),
        # we make sure that we add 1 * that ballon * 1 (using l and r pointers), and
        # then find the recursive sum of the remaining subarrays of balloons that are
        # to its left, and to its right. These subarrays can be classified as taking i,
        # the current index/ballon to pop last, and identifying the left subarray as
        # dfs(l, i - 1) so all ballons to its left up until left boundary, and the right
        # can be defined as dfs(i + 1, r) so all the balloons to its right up until the
        # right boundary. Once we have the recursive sums/maxes of these subarrays, we
        # can add them to our current count of the balloon we chose to pop last. This
        # way we can reduce repeated work if we see the same subarray being computed
        # again (if we need to compute the same (l, r) indeces), when we proceed with
        # the loop and choose a different balloon to pop last. The base case is to stop
        # shrinking the subarrays we check (left and right), when the pointers cross one
        # another, or in other words when l > r, thats the smallest possible subproblem