class Solution:
    # NeetCode Solution Explanation from Youtube
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitarray = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def backtrack(i, currentstring):
            if len(currentstring) == len(digits):
                res.append(currentstring)
                return
            for c in digitarray[digits[i]]:
                backtrack(i + 1, currentstring + c)

        if digits:
            backtrack(0, "")
        return res
