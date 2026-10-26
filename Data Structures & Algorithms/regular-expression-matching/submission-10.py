class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)

        dp = {}
        def dfs(i: int, j: int) -> bool:
            if j == m:
                return i == n
            if (i, j) in dp:
                return dp[(i, j)]
            
            matched = i < n and (s[i] == p[j] or p[j] == '.')
            if j + 1 < m and p[j + 1] == '*':
                dp[(i, j)] = (
                    dfs(i, j + 2) or
                    matched and dfs(i + 1, j)
                )
                return dp[(i, j)]
            if matched:
                dp[(i, j)] = dfs(i + 1, j + 1)
                return dp[(i, j)]
            
            dp[(i, j)] = False
            return dp[(i, j)]

        return dfs(0, 0)

        # s[i] == the char looked at in s, and p[j] == the char looked at in p.
        # The hard part about this problem isnt the dp, its even figuring out the brute
        # force approach. Think a bit sort of like an NFA, if we recognize that we find
        # a *, we know we can either take none, or take infinity amounts of it. Before
        # we deal with *, we want to know if what we are starring is correct/matching.
        # so we check whether s[i] == p[j] or if p[j] == '.' since '.' is a wildcard. If
        # either of those are true, we know we can proceed. Now if either of those are
        # true and we dont have a star afterwards, we can simply continue recursing
        # through and bump to the next char in both s and p to check, but if we do in
        # fact see a *, then we know we have another decision to make.
        # This decision involves skipping or choosing. So we take either possibility as
        # our answer for that step in the recursion. More precisely, if we skip it, then
        # we stay at the same letter we are checking in s, but then move 2 characters up
        # in p, as we need to skip over the char and the * symbol to reach next char.
        # now that we understand how the brute force approach works, we can understand
        # the caching of subproblems and the base case. The based case means, if we have
        # read all of the characters in p to match to s / reached end of the pattern,
        # we return wether we have also sucesfully reached the end of s / recreated the
        # full string of s by using the pattern. Now for the caching. At each step we
        # can see wether we have already been there before, even by making a different
        # prior choice (like skipping/taking a char that was *), if we have it means we
        # have fully found out wether s can be made from the pattern already if we have
        # reached that position, and that is the subproblem that we return.