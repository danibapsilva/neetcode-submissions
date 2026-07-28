class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix[0]) - 1

        top, bottom = 0, len(matrix) - 1
        row = 0
        while top <= bottom:
            middleRow = top + (bottom - top) // 2
            if matrix[middleRow][0] <= target <= matrix[middleRow][-1]:
                row = middleRow
                break
            elif target > matrix[middleRow][0]:
                top = middleRow + 1
            else:
                bottom = middleRow - 1
        
        print(row)
        while l <= r:
            middle = l + (r - l) // 2
            if target == matrix[row][middle]:
                return True
            elif target > matrix[row][middle]:
                l = middle + 1
            else:
                r = middle - 1
        
        return False
            
