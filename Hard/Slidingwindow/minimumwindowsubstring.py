import collections


class Solution:
    def minWindow(self, source: str, target: str) -> str:
        # need is a Counter for the characters we need to include from target
        needed_chars = collections.Counter(target)
        # Total count of characters we need to include
        missing_count = len(target)
        # Initialize pointers for the sliding window
        start_window = min_start = min_end = 0
        # Enumerate over the source string with index starting at 1
        for end_window, char in enumerate(source, 1):
            # Decrease the missing count if the character is needed
            missing_count -= needed_chars[char] > 0
            needed_chars[char] -= 1
            # If no characters are missing, try to shrink the window from the left
            if missing_count == 0:
                while start_window < end_window and needed_chars[source[start_window]] < 0:
                    needed_chars[source[start_window]] += 1
                    start_window += 1
                # Update the minimum window if the current one is smaller
                if not min_end or end_window - start_window <= min_end - min_start:
                    min_start, min_end = start_window, end_window
        # Return the minimum window from the source string
        return source[min_start:min_end]
    def minWindow2(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # Create a dictionary to store the frequency of characters in 't'
        char_count = {}
        for char in t:
            char_count[char] = char_count.get(char, 0) + 1

        # Initialize variables for the sliding window
        left = 0
        min_len = float('inf')
        min_window = ""
        char_found = 0

        # Start and end pointers of the sliding window
        for right in range(len(s)):
            # If the character at the right pointer is in 't', decrement its count in 'char_count'
            if s[right] in char_count:
                char_count[s[right]] -= 1
                if char_count[s[right]] >= 0:
                    char_found += 1

            # If all characters in 't' are found in the current window
            while char_found == len(t):
                # Update the minimum window if needed
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_window = s[left:right + 1]

                # Move the left pointer to shrink the window
                if s[left] in char_count:
                    char_count[s[left]] += 1
                    if char_count[s[left]] > 0:
                        char_found -= 1

                left += 1

        return min_window