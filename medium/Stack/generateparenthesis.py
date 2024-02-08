class Solution:
    def generateParenthesis(self, n):
        # Helper function to generate valid parentheses combinations
        def generate(p, left, right, parens=[]):
            if left:  # If there are still opening parentheses left to add
                generate(p + '(', left - 1, right)
            if right > left:  # If adding a closing parenthesis is valid
                generate(p + ')', left, right - 1)
            if not right:  # When all parentheses are used
                parens += p,
            return parens

        return generate('', n, n)
    # neetcode
    #---------------DO UPVOTE IF IT HELPS YOU--------------
    def generateParenthesis_nc(self, n):
        res = []
        stack = []
        def backTrack(openN , closedN):
            if openN == closedN ==n:
                res.append("".join(stack))
                return 
            if openN < n:
                stack.append("(")
                backTrack(openN+1 , closedN )
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backTrack(openN , closedN+1)
                stack.pop()
        backTrack(0,0)
        return res

        