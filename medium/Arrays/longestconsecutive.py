class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:  # If the list is empty, return 0
            return 0

        nums.sort()
        longest_streak = 1
        current_streak = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:  # Check for non-duplicate
                if nums[i] == nums[i - 1] + 1:  # Check if the current number is consecutive
                    current_streak += 1
                else:
                    longest_streak = max(longest_streak, current_streak)
                    current_streak = 1  # Reset the current streak for the new sequence
            # If nums[i] == nums[i - 1], it's a duplicate, and we do nothing

        # Compare the last streak after the loop ends
        return max(longest_streak, current_streak)

    def longestConsecutive2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        num_set = set(nums)
        max_length = 0
        for num in num_set:
            if num - 1 not in num_set:  # Check if num is the start of a sequence
                current_num = num
                current_length = 1

                while current_num + 1 in num_set:  # Extend the sequence
                    current_num += 1
                    current_length += 1

                max_length = max(max_length, current_length)

        return max_length
