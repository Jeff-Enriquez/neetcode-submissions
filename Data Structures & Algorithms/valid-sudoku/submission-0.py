class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        is_seen: set[str]

        # Check if rows are valid
        for row in range(9):
            is_seen = set()
            for col in range(9):
                if board[row][col] in is_seen:
                    return False
                elif board[row][col] != ".":
                    is_seen.add(board[row][col])
        
        # Check if columns are valid
        for col in range(9):
            is_seen = set()
            for row in range(9):
                if board[row][col] in is_seen:
                    return False
                elif board[row][col] != ".":
                    is_seen.add(board[row][col])

        # Check if squares are valid
        def check_square(start_row: int, start_col: int) -> bool:
            """
            Checks if a 3x3 square is valid. Must give the index of the top left position.
            """
            local_is_seen: set[str] = set()
            for row in range(start_row, start_row + 3):
                for col in range(start_col, start_col + 3):
                    if board[row][col] in local_is_seen:
                        print(str(local_is_seen))
                        return False
                    elif board[row][col] != ".":
                        local_is_seen.add(board[row][col])
            return True
        
        for row in range(0, 7, 3):
            for col in range(0, 7, 3):
                print(str(row) + ' ' + str(col))
                if not check_square(row, col):
                    return False
        
        return True
