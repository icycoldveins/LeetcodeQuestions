class Solution:
    def twoSum(self, numbers, targetSum):
        numberToIndexMap = {}
        for index, number in enumerate(numbers):
            complement = targetSum - number 
            if complement in numberToIndexMap:
                return [numberToIndexMap[complement], index]
            numberToIndexMap[number] = index
