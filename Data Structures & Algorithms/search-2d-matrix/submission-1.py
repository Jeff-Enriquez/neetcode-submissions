class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        row_len = len(matrix[0])
        l: int = 0
        r: int = len(matrix) * row_len - 1
        while l <= r:
            mid: int = l + (r - l) // 2
            curr: int = matrix[mid // row_len][mid % row_len]
            if target == curr:
                return True
            elif target < curr:
                r = mid - 1
            else:
                l = mid + 1

        return False