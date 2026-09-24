class Solution:
    def search(self, nums: list[int], target: int) -> int:
        return self.binary_search(nums, target)
    
    def binary_search(self, nums: list[int], target: int) -> int:
        def helper(l: int, r: int) -> int:
            print("l: " + str(l) + " r: " + str(r))
            if l > r:
                return -1
            mid: int = l + (r - l) // 2
            if target == nums[mid]:
                return mid
            elif target < nums[mid]:
                return helper(l, mid - 1)
            else:
                return helper(mid + 1, r)
        
        return helper(0, len(nums) - 1)

