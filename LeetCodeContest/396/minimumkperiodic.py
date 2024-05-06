class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        portions = {}
        numPortions = len(word) // k
        for i in range(numPortions):
            portion = word[i * k: (i + 1) * k]
            portions[portion] = portions.get(portion, 0) + 1

        return numPortions - max(portions.values())


# Example input
word = "leetcodeleet"
k = 4

# Create an instance of the Solution class
sol = Solution()

# Call the method with the example input
result = sol.minimumOperationsToMakeKPeriodic(word, k)
print("Minimum number of operations required:", result)
