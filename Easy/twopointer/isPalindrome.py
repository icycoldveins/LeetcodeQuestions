class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left, right = 0, len(s) - 1

        while left < right:
            # Move the left pointer to the right until it points to an alphanumeric character
            while left < right and not s[left].isalnum():
                left += 1

            # Move the right pointer to the left until it points to an alphanumeric character
            while left < right and not s[right].isalnum():
                right -= 1

            # Compare the characters at the left and right pointers
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True

# alternative solution
# 1 class Solution(object):
# 2    def isPalindrome(self, s):
# 3        """
# 4        :type s: str
# 5        :rtype: bool
# 6        """
# 7        # Filter out non-alphanumeric characters and convert to lowercase
# 8        filtered_chars = [char.lower() for char in s if char.isalnum()]
# 9
# 10       # Check if the filtered string is a palindrome
# 11       return filtered_chars == filtered_chars[::-1]
