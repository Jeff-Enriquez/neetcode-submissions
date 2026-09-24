class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l: int = 0
        r: int = len(nums) - 1
        while l <= r:
            mid: int = l + (r - l) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        
        return -1
