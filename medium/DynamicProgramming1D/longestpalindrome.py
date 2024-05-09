class Solution:
    # def longestPalindrome(self, s: str) -> str:
    #     res = ""
    #     resLen = 0
    #     for i in range(len(s)):
    #         l, r = i, i
    #         while l >= 0 and r < len(s) and s[l] == s[r]:
    #             if (r - l + 1) > resLen:
    #                 res = s[l:r + 1]
    #                 resLen = r - l + 1
    #             l -= 1
    #             r += 1
    #         # even length
    #         l, r = i, i + 1
    #         while l >= 0 and r < len(s) and s[l] == s[r]:
    #             if (r - l + 1) > resLen:
    #                 res = s[l:r + 1]
    #                 resLen = r - l + 1
    #             l -= 1
    #             r += 1
    #     return res

    def longestPalindrome(self, s: str) -> str:
        # dp approach
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = [0, 0]

        for start in range(n):
            dp[start][start] = True

        for start in range(n - 1):
            if s[start] == s[start + 1]:
                dp[start][start + 1] = True
                ans = [start, start + 1]

        for diff in range(2, n):
            for start in range(n - diff):
                end = start + diff
                if s[start] == s[end] and dp[start + 1][end - 1]:
                    dp[start][end] = True
                    ans = [start, end]

        start, end = ans
        return s[start: end + 1]


solution = Solution()

# Define the input string
input_string = "babad"


# Call the countSubstrings method with the input string
result = solution.longestPalindrome(input_string)

# Print the result
print("Number of palindromic substrings in 'level':", result)
