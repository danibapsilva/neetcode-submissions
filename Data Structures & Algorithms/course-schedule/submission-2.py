class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preqMap = defaultdict(list)
        for crse, preq in prerequisites:
            preqMap[crse].append(preq)

        canBeFinished, exploring = set(), set()
        def dfs(course: int) -> bool:
            if course in canBeFinished:
                return True
            if course in exploring:
                return False
            
            exploring.add(course)
            for preq in preqMap[course]:
                if not dfs(preq):
                    return False

            exploring.remove(course)
            canBeFinished.add(course)
            return True

        for courseNumber in range(numCourses):
            if not dfs(courseNumber):
                return False
        return True