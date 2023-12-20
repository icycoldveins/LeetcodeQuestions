class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        # Function to check if a sequence starting with num1 and num2 is additive
        def check(num1, num2, start):
            if start == n:  # If reached the end of the string
                return True
            sum_str = str(int(num1) + int(num2))
            sum_len = len(sum_str)
            if start + sum_len > n or num[start:start + sum_len] != sum_str:
                return False
            return check(num2, sum_str, start + sum_len)

        for i in range(1, n):
            for j in range(i + 1, n):
                num1, num2 = num[:i], num[i:j]
                # Skip if any number has leading zero and is not zero
                if (num1 != "0" and num1.startswith('0')) or (num2 != "0" and num2.startswith('0')):
                    continue
                if check(num1, num2, j):
                    return True
        return False
