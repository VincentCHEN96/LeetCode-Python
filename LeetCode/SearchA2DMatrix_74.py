class Solution:
    def searchMatrix(self, matrix: [[int]], target: int) -> bool:
        if len(matrix) == 0:
            return False

        low = 0
        high = len(matrix) * len(matrix[0]) - 1

        while low <= high:
            mid = int((low + high) / 2)
            mid_num = matrix[int(mid / len(matrix[0]))][mid % len(matrix[0])]
            if target < mid_num:
                high = mid - 1
            elif target > mid_num:
                low = mid + 1
            else:
                return True
        return False
