class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge(arr: List[int], L: int, M: int, R: int) -> None:
            left, right = arr[L: M + 1], arr[M + 1: R + 1]
            n, m = len(left), len(right)

            i, j, k = L, 0, 0
            while j < n and k < m:
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = right[k]
                    k += 1
                i += 1
            
            while j < n:
                arr[i] = left[j]
                i, j = i + 1, j + 1
            while k < m:
                arr[i] = right[k]
                i, k = i + 1, k + 1
            
            return arr

        def mergeSort(arr: List[int], l: int, r: int) -> None:
            if l >= r:
                return
            
            middle = l + (r - l) // 2
            mergeSort(arr, l, middle)
            mergeSort(arr, middle + 1, r)

            merge(arr, l, middle, r)

        n = len(nums)
        mergeSort(nums, 0, n)

        return nums
        
        # We recursively divide the array into smaller subarrays until the
        # smallest subarray is of length one, since one element arrays are
        # inherently sorted. We do this with the recursive function
        # mergeSort. We then conquer/merge each divided subarray, noticing
        # the fact that each subarray has already been sorted by a prior
        # recursive call. We do this with the helper function merge.
        # We keep track of 3 pointers/vars that store the current index
        # of the parent array that we will fill the next sorted element
        # into, i, the current index of the left subarray we are looking
        # at, j, & the current index of the right subarray we are looking
        # at, k. We make sure to increment those 3 pointers
        # correspondingly to their array.