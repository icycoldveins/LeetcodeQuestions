class Solution(object):
    def lengthOfLongestSubstring(self, string):
        uniqueCharacters = set()
        maxLengthFound = 0
        windowStart = 0
        for windowEnd in range(len(string)):
            while string[windowEnd] in uniqueCharacters:
                uniqueCharacters.remove(string[windowStart])
                windowStart += 1
            uniqueCharacters.add(string[windowEnd])
            maxLengthFound = max(maxLengthFound, windowEnd - windowStart + 1)
        return maxLengthFound
