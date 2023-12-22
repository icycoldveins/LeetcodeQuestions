class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """

        # Count total number of ones in the entire string
        total_ones = s.count('1')

        # Initialize the count of zeroes and the maximum score
        count_zeroes = 0
        max_score = 0

        # Iterate through the string (excluding the last character as the split must be non-empty)
        for i in range(len(s) - 1):  # Notice range is till len(s) - 1
            if s[i] == '0':
                count_zeroes += 1
            else:
                total_ones -= 1  # One less 1 to be considered for the right part

            # Calculate the score at this split
            current_score = count_zeroes + total_ones
            max_score = max(max_score, current_score)

        return max_score
