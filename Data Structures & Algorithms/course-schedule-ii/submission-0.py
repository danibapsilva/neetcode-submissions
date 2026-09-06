class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preqMap = {i: [] for i in range(numCourses)}
        for courseNumber, preq in prerequisites:
            preqMap[courseNumber].append(preq)
        
        res, exploring, canBeFinished = [], set(), set()
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

            res.append(courseNumber)
            return True
        
        for courseNumber in range(numCourses):
            if not dfs(courseNumber):
                return []
        return res
