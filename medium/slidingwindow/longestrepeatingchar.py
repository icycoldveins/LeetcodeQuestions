class Solution:
    def characterReplacement(self, string, maxReplacements):
        charFrequency = {}
        maxFreq = 0
        windowStart = 0
        longestSubstrLength = 0

        for windowEnd in range(len(string)):
            currentChar = string[windowEnd]
            charFrequency[currentChar] = charFrequency.get(currentChar, 0) + 1

            maxFreq = max(maxFreq, charFrequency[currentChar])

            if (windowEnd - windowStart + 1) - maxFreq > maxReplacements:
                leftChar = string[windowStart]
                charFrequency[leftChar] -= 1
                windowStart += 1

            longestSubstrLength = max(
                longestSubstrLength, windowEnd - windowStart + 1)

        return longestSubstrLength
