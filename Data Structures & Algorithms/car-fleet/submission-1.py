class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        pairs = sorted(pair for pair in zip(position, speed))
        for pos, spd in pairs[::-1]:
            time = float((target - pos)) / spd
            stack.append(time)
            if len(stack) > 1 and time <= stack[-2]:
                stack.pop()


        return len(stack)