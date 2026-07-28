class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix[0])
        for i in range(len(matrix)):
            if target > matrix[i][-1]:
                continue
            while l <= r:
                middle = l + (r - l) // 2
                if target == matrix[i][middle]:
                    return True
                elif target > matrix[i][middle]:
                    l = middle + 1
                else:
                    r = middle - 1
        
        return False
            
