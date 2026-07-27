class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pairs = sorted([[p, s] for [p, s] in zip(position, speed)])
        print(pairs)
        for pos, spd in pairs[::-1]:
            time = float((target - pos)) / spd
            print(time)
            stack.append(time)
            if len(stack) > 1 and time <= stack[-2]:
                stack.pop()


        return len(stack)