class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        output = [1] * n

        # Calculate left products
        left_product = 1
        for i in range(n):
            output[i] = left_product
            print(f"After index {i}, left_product: {left_product}, output: {output}")
            left_product *= nums[i]

        # Calculate right products and update output array
        right_product = 1
        for i in range(n - 1, -1, -1):
            output[i] *= right_product
            print(f"At index {i}, right_product: {right_product}, output: {output}")
            right_product *= nums[i]

        return output

# Example usage
sol = Solution()
result = sol.productExceptSelf([1, 2, 3, 4])
print("Final output:", result)
