class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Create a dictionary that maps opening brackets to their corresponding closing brackets.
        d = {'(': ')', '{': '}', '[': ']'}

        # Create an empty stack to keep track of the opening brackets.
        stack = []

        # Iterate through each character in the input string.
        for i in s:
            if i in d:  # If the character is an opening bracket (rule 1)
                stack.append(i)  # Push it onto the stack.
            # If it's a closing bracket (rule 2)
            elif len(stack) == 0 or d[stack.pop()] != i:
                # If the stack is empty or the brackets don't match, return False.
                return False

        # After processing all characters, check if there are any unmatched opening brackets left (rule 3).
        # If the stack is empty, all brackets matched, so return True. Otherwise, return False.
        return len(stack) == 0

# Comments explaining the rules:
# 1. If the character is an opening bracket, push it onto the stack.
# 2. If it's a closing bracket, check if the stack is empty or if the brackets don't match; return False in such cases.
# 3. After processing all characters, check if there are any unmatched opening brackets left on the stack; return True if the stack is empty, else return False.
