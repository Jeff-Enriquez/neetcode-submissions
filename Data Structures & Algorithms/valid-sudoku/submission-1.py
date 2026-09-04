"""
Module to validate a Sudoku board.
"""

class Solution:
    """
    A class to provide functionality for validating a Sudoku board.
    """
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        """
        Checks if a given Sudoku board is valid.

        Args:
            board: A 9x9 list of lists representing the Sudoku board.

        Returns:
            True if the board is valid, False otherwise.
        """
        is_seen: set[str] = set()

        # Check if rows are valid
        for row in range(9):
            is_seen.clear()
            for col in range(9):
                if board[row][col] in is_seen:
                    return False
                elif board[row][col] != ".":
                    is_seen.add(board[row][col])
        
        # Check if columns are valid
        for col in range(9):
            is_seen.clear()
            for row in range(9):
                if board[row][col] in is_seen:
                    return False
                elif board[row][col] != ".":
                    is_seen.add(board[row][col])

        # Check if squares are valid
        def check_square(start_row: int, start_col: int) -> bool:
            """
            Checks if a 3x3 square is valid. Must give the index of the top left position.

            Args:
                start_row: The starting row index of the 3x3 square.
                start_col: The starting column index of the 3x3 square.

            Returns:
                True if the square is valid, False otherwise.
            """
            nonlocal is_seen
            is_seen.clear()
            for row in range(start_row, start_row + 3):
                for col in range(start_col, start_col + 3):
                    if board[row][col] in is_seen:
                        return False
                    elif board[row][col] != ".":
                        is_seen.add(board[row][col])
            return True
        
        for row in range(0, 7, 3):
            for col in range(0, 7, 3):
                if not check_square(row, col):
                    return False
        
        return True
