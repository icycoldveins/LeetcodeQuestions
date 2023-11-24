"""  
You are given a string s and an integer k. 
You can choose any character of the string and change it 
to any other uppercase English character. 
You can perform this operation at most k times.
Return the length of the longest substring containing the same 
letter you can get after performing the above operations.
"""
class Solution:
    def characterReplacement(self, s, k):
        count = {}
        max_count = 0
        left = 0
        longest = 0

        for right in range(len(s)):
            count[s[right]] = count.get(s[right], 0) + 1
            max_count = max(max_count, count[s[right]])

            # Print the status after each character addition
            print(
                f"Window [{left}, {right}]: {s[left:right+1]}, Count: {count}, Max Count: {max_count}")

            if (right - left + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1
                print(
                    f"Shrinking window to [{left}, {right}]: {s[left:right+1]}")

            longest = max(longest, right - left + 1)

        print(f"Longest Substring Length: {longest}")
        return longest


# Example usage
sol = Solution()
sol.characterReplacement("AABBC", 1)
