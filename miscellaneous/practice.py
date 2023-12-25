class Solution:
    def minOperations(self, s: str) -> int:
        # Initialize counts for both patterns
        count0, count1 = 0, 0

        for i in range(len(s)):
            # Check for Pattern 1 (starting with '0')
            if s[i] != str(i % 2):  # i % 2 is 0 for even indices and 1 for odd indices
                count0 += 1

            # Check for Pattern 2 (starting with '1')
            # (i + 1) % 2 is 1 for even indices and 0 for odd indices
            if s[i] != str((i + 1) % 2):
                count1 += 1

        # Return the minimum of the two counts
        return min(count0, count1)

# Example Usage:
# s = "0100"
# sol = Solution()
# print(sol.minOperations(s))  # Output will be 1 for this example
