class Solution:
    def findMin(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if nums[-1] < nums[-2]:
            return nums[-1]
        return self.binary_search(nums, 0, len(nums) - 1)
    
    # Find index where mid is less than the number to left
    def binary_search(self, nums: list[int], l, r) -> int:
        if l > r or l == r:
            return -1001
        mid: int = ((r - l) // 2) + l
        print("l: " + str(l) + " r: " + str(r) + " mid: " + str(mid))
        if nums[mid] < nums[mid - 1]:
            return nums[mid]
        left: int = self.binary_search(nums, l, mid)
        right: int = self.binary_search(nums, mid + 1, r)
        return max(left, right)
