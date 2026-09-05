class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        """Find two indices such that the numbers at those indices add up to the target.

        Args:
            numbers: A list of integers.
            target: The target sum.

        Returns:
            A list containing the 1-based indices of the two numbers that add up to the target.
        """
        left_idx: int = 0
        right_idx: int = len(numbers) - 1
        curr_sum: int = numbers[0] + numbers[right_idx]
        while curr_sum != target:
            if curr_sum > target:
                curr_sum -= numbers[right_idx]
                right_idx -= 1
                curr_sum += numbers[right_idx]
            else:
                curr_sum -= numbers[left_idx]
                left_idx += 1
                curr_sum += numbers[left_idx]
        return [left_idx + 1, right_idx + 1]
