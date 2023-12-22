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
