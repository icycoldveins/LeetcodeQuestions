class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        uniqueset = set()
        start = 0
        longestlength=0
        for end in range(len(s)):
            while s[end] in uniqueset:
                uniqueset.remove(s[start])
                start +=1
            uniqueset.add(s[end])
            longestlength=max(longestlength,end-start+1)
        return longestlength