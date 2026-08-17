class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = sorted([p for p in zip(position, speed)])

        stack = []
        for pos, spd in pairs:
            time = float(target - pos) / spd
            while stack and stack[-1] <= time:
                stack.pop()
            stack.append(time)
        
        return len(stack)