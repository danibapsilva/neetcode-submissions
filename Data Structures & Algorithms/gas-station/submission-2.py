class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        if sum(gas) < sum(cost):
            return -1
        
        res = total = 0
        for i in range(n):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                res = i + 1
        return res
    

        # if there is a possible solution (sum of gas is >= sum of cost), we know that
        # there is only one unique solution, given the prompt, so we know that whenever
        # we find/calculate an invalid starting position, the only possible solution
        # to the problem, has to come after it, so we greedily set the result to the
        # next index.