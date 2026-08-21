class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr)
        res = []
        while l < r:
            middle = l + (r - l) // 2
            if arr[middle] < x:
                l = middle + 1
            else:
                r = middle
        
        left, right = l - 1, l
        while len(res) < k:
            if left < 0:
                res.append(arr[right])
                right += 1
            elif right >= len(arr):
                res.append(arr[left])
                left -= 1
            elif abs(arr[left] - x) <= abs(arr[right] - x):
                res.append(arr[left])
                left -= 1
            else:
                res.append(arr[right])
                right += 1
        
        return sorted(res)
         