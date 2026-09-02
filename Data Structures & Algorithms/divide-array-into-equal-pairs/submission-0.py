class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1
        
        for num in freq:
            if freq[num] % 2:
                return False
        return True