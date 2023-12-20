class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        result = []
        for left in range(len(nums)-2):
            if left > 0 and nums[left] == nums[left-1]:
                continue
            mid = left+1
            right = len(nums)-1
            while mid < right:
                currentsum = nums[left]+nums[mid]+nums[right]
                if currentsum<0:
                    mid +=1
                elif currentsum>0:
                    right-=1
                else:
                    result.append([nums[left],nums[mid],nums[right]])
                    while mid<right and nums[mid]==nums[mid+1]:
                        mid +=1
                    while mid<right and nums[right]==nums[right-1]:
                        right -=1
                    right-=1
                    mid +=1
        return result
                    