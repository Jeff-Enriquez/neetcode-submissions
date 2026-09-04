class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr_majority: int = nums[0]
        curr_count: int = 1
        for i in range(1, len(nums)):
            if nums[i] == curr_majority:
                curr_count += 1
            elif curr_count == 1:
                curr_majority = nums[i]
            else:
                curr_count -= 1
        return curr_majority