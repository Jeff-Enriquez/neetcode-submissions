class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        """Returns the product of all elements in the array except the element at the current index.

        Args:
            nums: A sequence of integers.

        Returns:
            A list of integers where each element is the product of all elements in the input list except the element at the current index.
        """
        ltr_product_sum: list[int] = [1]
        for i in range(len(nums)):
            ltr_product_sum.append(ltr_product_sum[i] * nums[i])

        rtl_product_sum: list[int] = [0] * (len(nums) + 1)
        rtl_product_sum[len(nums)] = 1
        for i in range(len(nums) - 1, -1, -1):
            rtl_product_sum[i] = rtl_product_sum[i + 1] * nums[i]

        result: list[int] = []
        for i in range(len(nums)):
            result.append(ltr_product_sum[i] * rtl_product_sum[i + 1])

        return result