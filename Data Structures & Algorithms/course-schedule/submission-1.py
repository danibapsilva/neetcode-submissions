class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preqMap = {i: [] for i in range(numCourses)}
        for courseNumber, preq in prerequisites:
            preqMap[courseNumber].append(preq)

        exploring, canBeFinished = set(), set()
        def dfs(courseNumber: int) -> bool:
            if courseNumber in exploring:
                return False
            if courseNumber in canBeFinished:
                return True
            
            exploring.add(courseNumber)
            for preq in preqMap[courseNumber]:
                if not dfs(preq):
                    return False
            exploring.remove(courseNumber)
            canBeFinished.add(courseNumber)
            return True
        
        for courseNumber in range(numCourses):
            if not dfs(courseNumber):
                return False
        return True