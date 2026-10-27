class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [pair for pair in zip(position, speed)]
        
        stack = []
        for position, speed in sorted(pairs)[::-1]:
            distance = target - position
            time = float(distance) / speed
            
            if not stack or time > stack[-1]:
                stack.append(time)

        return len(stack)