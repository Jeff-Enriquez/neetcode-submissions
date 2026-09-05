class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        """Returns all unique triplets in the array which gives the sum of zero.

        Args:
            nums: A list of integers.

        Returns:
            A list of lists of integers, where each inner list contains three integers that sum to zero.
        """
        triplets: list[list[int]] = []
        num_len: int = len(nums)
        nums.sort()
        nums.append(nums[num_len - 1] + 1)
        for i in range(num_len - 1, -1, -1):
            if nums[i] == nums[i + 1]:
                continue
            left_idx: int = 0
            right_idx: int = i - 1
            target: int = nums[i] * -1
            while left_idx < right_idx:
                value: int = nums[left_idx] + nums[right_idx]
                if value < target:
                    left_idx += 1
                elif value > target:
                    right_idx -= 1
                else:
                    triplets.append([nums[i], nums[left_idx], nums[right_idx]])
                    left_idx += 1
                    right_idx -= 1
                    while left_idx < right_idx and nums[right_idx + 1] == nums[right_idx]:
                        right_idx -= 1
        return triplets
