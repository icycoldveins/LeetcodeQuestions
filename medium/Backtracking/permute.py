class Solution:
    def permute(self, nums):
        def backtrack(first=0):
            if first == n:
                output.append(nums[:])
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]  # Swap
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]  # Swap back

        n = len(nums)
        output = []
        backtrack()
        return output   
    def permute2(self, nums):
        
        res = []
        def dfs(path, num): # record the path and remaining numbers
            if not num:
                res.append(path)    # When finished iterating, append path to result
                return
            for i in range(len(num)):
                dfs(path + [num[i]], num[:i] + num[i + 1:]) 
                # append the current number to path and iterate with the unused numbers
        
        dfs([], nums)
        return res  # return results   
    