class Solution:
    def evalRPN(self, tokens):
        stack = []
        operators = {'*', '+', '/', '-'}
        for token in tokens:
            if token in operators:
                b, a = stack.pop(), stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    if a * b >= 0:
                        stack.append(a//b)
                    else:
                        stack.append(-(-a//b))
            else:
                stack.append(int(token))
        return stack[0]
        """
        :type tokens: List[str]
        :rtype: int
        """
