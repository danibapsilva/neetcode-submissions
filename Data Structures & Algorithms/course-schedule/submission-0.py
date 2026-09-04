class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # EX 1: look at 0, need to take 1 first, look for 1 prereqs, none
        # so we take 1, decrement numcount -= 1, then take mark prereq found?
        # then take 0, decrement numcount -= 1, numcount == 0, so True
        # EX 2: look at 0, need to take 1 first, look for 1, 1 needs to take 0 first
        # that will create a cycle, so we stop searching 0, and move onto 1,
        # same thing happens so we stop, numcount is still at 2 != 0 so False

        preqMap = {i: [] for i in range(numCourses)}
        for crse, preq in prerequisites:
            preqMap[crse].append(preq)
        
        exploring, canBeFinished = set(), set()
        def dfs(crse: int) -> bool:
            if crse in exploring:
                return False
            if crse in canBeFinished:
                return True
            
            exploring.add(crse)
            for preq in preqMap[crse]:
                if not dfs(preq):
                    return False

            exploring.remove(crse)
            canBeFinished.add(crse)
            return True
        
        for crse in range(numCourses):
            if not dfs(crse):
                return False
        return True