class Solution:
    def twoSum(self, numbers, targetSum):
        # Create an empty dictionary to store numbers and their indices.
        numberToIndexMap = {}
        # Loop through each element in the 'numbers' array.
        for index, number in enumerate(numbers):
            # Calculate the complement needed to reach the 'targetSum'.
            complement = targetSum - number
            # Check if the complement is already in the dictionary.
            if complement in numberToIndexMap:
                # If found, return the indices of the two numbers.
                return [numberToIndexMap[complement], index]
            # If not found, add the current number and its index to the dictionary.
            numberToIndexMap[number] = index

# The function returns the indices of the two numbers that add up to 'targetSum'.
