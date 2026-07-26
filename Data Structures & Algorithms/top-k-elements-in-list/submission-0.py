class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for i in nums:
            dic[i] = dic.get(i, 0) + 1
        
        return sorted(dic, key=lambda x: dic[x], reverse=True)[:k]
