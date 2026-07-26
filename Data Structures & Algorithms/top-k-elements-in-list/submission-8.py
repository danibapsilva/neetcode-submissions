class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        buckets = [[] for _ in range(len(nums) + 1)]
        for num in freq:
            buckets[freq[num]].append(num)

        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res

        return []