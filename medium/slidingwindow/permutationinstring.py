class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        # Initialize frequency counters with more descriptive names
        freq_s1 = [0] * 26  # Frequency of each character in s1
        # Frequency of each character in the current window of s2
        freq_window_s2 = [0] * 26

        # Populate frequency counter for s1
        for char_s1 in s1:
            freq_s1[ord(char_s1) - ord('a')] += 1

        # Sliding window over s2
        for window_end in range(len(s2)):
            freq_window_s2[ord(s2[window_end]) - ord('a')] += 1
            if window_end >= len(s1):
                # Remove the character leaving the window
                freq_window_s2[ord(s2[window_end - len(s1)]) - ord('a')] -= 1

            # Compare frequency counters
            if freq_s1 == freq_window_s2:
                return True

        return False
