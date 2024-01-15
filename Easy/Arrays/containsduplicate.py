class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        unique_value = set()
        for num in nums:
            if num in unique_value:
                return True
            unique_value.add(num)
        return False
