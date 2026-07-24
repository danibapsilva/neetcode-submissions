class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # INTUITIVE APPROACH
            # count = {}
            # for i in nums:
            #     count[i] = count.get(i, 0) + 1
            
            # return sorted(count, key=lambda x: count[x], reverse=True)[:k]

        # MIN-HEAP approach -> heapq sorted with min @indx 0
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        

        heap = []
        for num in freq.keys():
            heapq.heappush(heap, (freq[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1]) # tuple (num, freq) so index [1] grabs freq
        
        return res

        # BUCKET-SORT APPROACH -> index is the 0-n, n is len, with the value being the freq
