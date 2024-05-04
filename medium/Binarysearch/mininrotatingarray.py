from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums[0]
        l, r = 0, len(nums) - 1
        # [450123]
        # rotations mean that there are two sorted portions in the array
        # we can use the mid to find out where the pivot happens
        while l <= r:
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break
            mid = (l+r)//2
            res = min(res, nums[mid])
            if nums[mid] >= nums[l]:
                l = mid+1
            else:
                r = mid-1
        return res


solution = Solution()
print(solution.findMin([4, 5, 1, 2, 3]))
