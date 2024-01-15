class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        output = [1] * n

        # Calculate left products
        left_product = 1
        for i in range(n):
            output[i] = left_product
            left_product *= nums[i]

        # Calculate right products and update output array
        right_product = 1
        for i in range(n - 1, -1, -1):
            output[i] *= right_product
            right_product *= nums[i]

        return output