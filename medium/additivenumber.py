class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        for i in range(1, n):
            for j in range(i+1, n):
                num1, num2 = num[:i], num[i:j]

                # Skip if numbers have leading zeros
                if (len(num1) > 1 and num1.startswith('0')) or (len(num2) > 1 and num2.startswith('0')):
                    continue

                while j < n:
                    sum = str(int(num1) + int(num2))
                    if not num.startswith(sum, j):
                        break
                    j += len(sum)
                    num1, num2 = num2, sum

                    if j == n:
                        return True

        return False
