class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_to_index = {}  # A dictionary to store number and its index in nums.

        # Iterate through each number in the array.
        for index, num in enumerate(nums):
            complement = target - num  # Calculate the complement of the current number.

            # Check if the complement is already in the dictionary.
            if complement in num_to_index:
                # If found, return the indices of the complement and the current number.
                return [num_to_index[complement], index]

            # If the complement is not found, add the current number and its index to the dictionary.
            num_to_index[num] = index

        # Since the problem statement guarantees a solution, the function will return before this point.
