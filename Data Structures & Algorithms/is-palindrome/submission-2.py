"""Module to check if a given string is a palindrome.

This module provides a class `PalindromeChecker` with a method `is_palindrome`
to determine if a string is a palindrome, ignoring non-alphanumeric characters
and case differences.
"""

class Solution:
    """Class to check if a given string is a palindrome.

    Attributes:
        None
    """
    
    def isPalindrome(self, s: str) -> bool:
        """Check if the given string is a palindrome.

        Args:
            s (str): The string to check.

        Returns:
            bool: True if the string is a palindrome, False otherwise.
        """
        left_idx: int = 0
        right_idx: int = len(s) - 1
        while left_idx < right_idx:
            if not (s[left_idx].isalpha() or s[left_idx].isnumeric()):
                left_idx += 1
            elif not (s[right_idx].isalpha() or s[right_idx].isnumeric()):
                right_idx -= 1
            elif s[left_idx].lower() != s[right_idx].lower():
                return False
            else:
                left_idx += 1
                right_idx -= 1
        return True
