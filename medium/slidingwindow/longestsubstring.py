class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen = 0
        start = 0
        uniqueset = set()
        for end in range(len(s)):
            while s[end] in uniqueset:
                uniqueset.remove(s[start])
                start += 1
            uniqueset.add(s[end])
            maxlen = max(maxlen, end-start+1)
        return maxlen
mapper=Solution()
mapper.lengthOfLongestSubstring("pwwkew")