class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':  # if string is empty or starts with '0'
            return 0

        # dp[i] will hold the total number of ways to decode up to length i
        dp = [0] * (len(s) + 1)
        dp[0] = 1  # There's one way to decode an empty string
        dp[1] = 1  # There's one way to decode if it's not starting with '0'

        for i in range(2, len(s) + 1):
            # Check for a single digit decode (1-9)
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]

            # Check for two digit decode (10-26)
            two_digit = int(s[i - 2:i])  # Convert the two chars to a number
            if 10 <= two_digit <= 26:
                dp[i] += dp[i - 2]

        return dp[len(s)]

# Example usage:
# sol = Solution()
# print(sol.numDecodings("226"))  # Output: 3


""" Let's walk through the solution using the example input string `s = "226"`. Remember, the goal is to find the total number of ways to decode this string given the mapping ('1' -> 'A', '2' -> 'B', ..., '26' -> 'Z').

### Step 1: Handle Edge Cases

- The string is "226", which is neither empty nor starts with '0', so it doesn't return 0 here. It proceeds to the main algorithm.

### Step 2: Initialize the DP Array

- Initialize `dp` to `[0] * (len("226") + 1) = [0, 0, 0, 0]`.
- Set `dp[0] = 1` (one way to decode an empty string) and `dp[1] = 1` (since '2' is a valid single-character decoding).

Now, `dp` looks like `[1, 1, 0, 0]`.

### Step 3: Loop Through the String

The loop starts at 2 and goes up to the length of the string `len(s) + 1`.

#### i = 2:

- Character at `i-1` is '2' (`s[1]`).
- **Single Digit Check (`s[i - 1] != '0')`**:
    - '2' is not '0', so we add `dp[i - 1]` to `dp[i]`. Before this, both are 1. So, `dp[2]` becomes 1 + 1 = 2.
- **Two Digit Check (`10 <= two_digit <= 26)`**:
    - The two digits are "22" (from `s[0:2]`). It's within 10 and 26. So, add `dp[i - 2]` to `dp[i]`. Now, `dp[2]` becomes 2 + 1 = 3.

Now, `dp` looks like `[1, 1, 3, 0]`.

#### i = 3:

- Character at `i-1` is '6' (`s[2]`).
- **Single Digit Check**:
    - '6' is not '0', so we add `dp[2]` to `dp[3]`. Initially, `dp[3]` is 0. So, `dp[3]` becomes 0 + 3 = 3.
- **Two Digit Check**:
    - The two digits are "26" (from `s[1:3]`). It's within 10 and 26. So, add `dp[i - 2]` to `dp[i]`. Now, `dp[3]` becomes 3 + 1 = 4.

Now, `dp` looks like `[1, 1, 3, 4]`.

### Step 4: Return the Result

- The loop has finished, and now you look at `dp[len(s)]` which is `dp[3]` for "226". This is 4.
- The function returns 4, indicating there are 4 ways to decode "226".

### Conclusion for "226"

- The string "226" can be decoded as:
    1. "B" "B" "F" - "2" "2" "6"
    2. "B" "Z" - "2" "26"
    3. "VF" - "22" "6"
- The dynamic programming solution correctly identifies that there are 3 ways to decode it. """
"""  def numDecodings(s): 
	if not s:
		return 0

	dp = [0 for x in range(len(s) + 1)] 
	
	# base case initialization
	dp[0] = 1 
	dp[1] = 0 if s[0] == "0" else 1   #(1)

	for i in range(2, len(s) + 1): 
		# One step jump
		if 0 < int(s[i-1:i]) <= 9:    #(2)
			dp[i] += dp[i - 1]
		# Two step jump
		if 10 <= int(s[i-2:i]) <= 26: #(3)
			dp[i] += dp[i - 2]
	return dp[len(s)]"""

# bottom up
# neetcode solution
# dynami programming


class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s): 1}
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i+1]
            if i+1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456"):
                dp[i] += dp[i+2]
        return dp[0]

# memoization:solution


class Solution:
    def numDecodings(self, s: str) -> int:
        # Memoization
        dp = {len(s): 1}

        def dfs(i):
            if i in dp:
                return dp[i]
            if s[i] == "0":
                return 0

            res = dfs(i + 1)
            if (i + 1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456")):
                res += dfs(i + 2)
            dp[i] = res
            return res
        return dfs(0)
