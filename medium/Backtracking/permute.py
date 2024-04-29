class Solution:
    def permute(self, nums):
        def backtrack(first=0):
            if first == n:
                output.append(nums[:])
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]  # Swap
                backtrack(first + 1)
                nums[first], nums[i] = nums[i], nums[first]  # Swap back

        n = len(nums)
        output = []
        backtrack()
        return output

    def permute2(self, nums):

        res = []

        def dfs(path, num):  # record the path and remaining numbers
            if not num:
                # When finished iterating, append path to result
                res.append(path)
                return
            for i in range(len(num)):
                dfs(path + [num[i]], num[:i] + num[i + 1:])
                # append the current number to path and iterate with the unused numbers

        dfs([], nums)
        return res  # return results

    def permute3(self, nums: List[int]) -> List[List[int]]:
        # base case
        if len(nums) == 1:
            return [[nums[0]]]

        # res stores the final permutations as we find them
        res = []
        for _ in range(len(nums)):
            # in this iteration, we are generating all permutations
            # ending in n
            n = nums.pop(0)

            # generate permutations of nums without n
            perms = self.permute(nums)

            for perm in perms:
                # create each of the permutations ending in n
                perm.append(n)

            # add to final result
            res.extend(perms)

            # add n to the end of nums
            # the next iteration will fetch the first element
            # in this way, we iterate through all elements of nums
            nums.append(n)

        return res
