class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Given a string s, find the length of the longest 
        # substring without repeating characters.
        charSet = set()
        maxLength = 0
        start = 0
        for end in range(len(s)):
            while s[end] in charSet:
                charSet.remove(s[start])
                start += 1
            charSet.add(s[end])
            maxLength = max(maxLength, end - start + 1)
        return maxLength
