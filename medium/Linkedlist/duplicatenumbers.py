from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: Finding the intersection point in the cycle
        slow, fast = 0, 0
        while True:
            slow = nums[slow]  # Move slow by 1 step
            fast = nums[nums[fast]]  # Move fast by 2 steps
            if slow == fast:  # Cycle detected when slow and fast meet
                break

        # Phase 2: Finding the entry point to the cycle, which is the duplicate
        slow2 = 0
        while True:
            slow = nums[slow]  # Move slow by 1 step
            slow2 = nums[slow2]  # Move slow2 by 1 step from the start
            if slow == slow2:  # Both meet at the duplicate number
                return slow


# Example usage
sol = Solution()
nums = [3, 1, 3, 4, 2]
print("The duplicate number is:", sol.findDuplicate(nums))
