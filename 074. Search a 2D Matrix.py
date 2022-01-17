class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        column = len(matrix[0])
        for i in range(row):
            left = 0
            right = column - 1
            while left <= right:
                mid = left + (right-left)//2
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] > target:
                    right = mid - 1
                elif matrix[i][mid] < target:
                    left = mid + 1
        return False

    
    ##不用for循环 一次二分查找
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or len(matrix)==0:
            return None

        row = len(matrix)
        column = len(matrix[0])
        left = 0
        right = row * column - 1
        while left <= right:
            mid = left + (right-left)//2
            x = matrix[mid//column][mid%column]
            if x == target:
                return True
            elif x > target:
                right = mid - 1
            elif x < target:
                left = mid + 1
        return False
