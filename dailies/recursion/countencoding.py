class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:  # Base case: When n is 1, return '1'.
            return '1'
        else:
            # Recursively call countAndSay with n - 1 to get the previous sequence.
            value = self.countAndSay(n - 1)
            count = 1  # Initialize count to 1.
            # Initialize an empty string to store the current sequence.
            tmp = ''

            # Iterate through the characters of the previous sequence.
            for i in range(len(value)):
                if i < len(value) - 1:
                    # If the current character is equal to the next character, increment count.
                    if value[i] == value[i + 1]:
                        count += 1
                    else:
                        # If the current character is different from the next one, append count and character to tmp.
                        tmp += str(count) + value[i]
                        count = 1  # Reset count to 1.
                else:
                    # If it's the last character of the sequence, append count and character to tmp.
                    tmp += str(count) + value[i]

            # Return the compressed sequence.
            return tmp
