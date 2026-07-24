class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # INTUITIVE APPROACH
            # count = {}
            # for i in nums:
            #     count[i] = count.get(i, 0) + 1
            
            # return sorted(count, key=lambda x: count[x], reverse=True)[:k]

        # MIN-HEAP APPROACH -> heapq sorted with min @indx 0
            # freq = {}
            # for num in nums:
            #     freq[num] = freq.get(num, 0) + 1
            

            # heap = []
            # for num in freq: # keys
            #     heapq.heappush(heap, (freq[num], num)) # sort heap by freq
            #     if len(heap) > k:
            #         heapq.heappop(heap)

            # res = []
            # for i in range(k):
            #     res.append(heapq.heappop(heap)[1]) # tuple (freq, num) so index [1] grabs num
            
            # return res

        # BUCKET-SORT APPROACH -> index is the 0-n, n is len, with the value being the freq
        freq = {}
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        buckets = [[] for _ in range(len(nums) + 1)] # +1 to include 0
        print("freq:", freq)
        for num in freq: # keys
            print("buckets:", buckets)
            buckets[freq[num]].append(num)
        
        res = []
        for i in range(len(buckets) -1, 0, -1):
            for num in buckets[i]:
                res.append(num)

                if len(res) == k:
                    return res
