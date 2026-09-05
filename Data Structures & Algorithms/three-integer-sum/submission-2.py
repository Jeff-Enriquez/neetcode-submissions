class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        triplets: list[list[int]] = []
        num_len: int = len(nums)
        prev_num: int = nums[0] - 1
        for i in range(num_len):
            if prev_num == nums[i]:
                continue
            else:
                prev_num = nums[i]
            left_idx: int = i + 1
            right_idx: int = num_len - 1
            target: int = nums[i] * -1
            while left_idx < right_idx:
                value: int = nums[left_idx] + nums[right_idx]
                if value < target:
                    left_idx += 1
                    while left_idx < right_idx and nums[left_idx - 1] == nums[left_idx]:
                        left_idx += 1
                elif value > target:
                    right_idx -= 1
                    while left_idx < right_idx and nums[right_idx + 1] == nums[right_idx]:
                        right_idx -= 1
                else:
                    triplets.append([nums[i], nums[left_idx], nums[right_idx]])
                    left_idx += 1
                    right_idx -= 1
                    while left_idx < right_idx and nums[right_idx + 1] == nums[right_idx]:
                        right_idx -= 1
                    while left_idx < right_idx and nums[left_idx - 1] == nums[left_idx]:
                        left_idx += 1
        return triplets