class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        left = [1] * n  # Initialize with all 1s for left products
        left_product = 1
        
        # Calculate left products
        for i in range(n):
            left[i] = left_product
            left_product *= nums[i]
        
        right_product = 1
        result = [0] * n
        
        # Calculate right products and update result
        for i in range(n - 1, -1, -1):
            result[i] = left[i] * right_product
            right_product *= nums[i]
        
        return result
