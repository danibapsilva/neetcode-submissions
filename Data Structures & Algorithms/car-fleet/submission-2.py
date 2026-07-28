class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [pair for pair in zip(position, speed)]

        stack = []
        for pos, spd in sorted(pairs)[::-1]:  # decreasing
            time = (float(target - pos)) / spd
            if stack and stack[-1] >= time:
                continue
            else:
                stack.append(time)
        
        return len(stack)