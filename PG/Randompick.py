import random


class Solution:

    def __init__(self, nums):
        self.nums = nums

    def pick(self, target: int) -> int:
        answer = []
        for idx, num in enumerate(self.nums):
            if target == num:
                answer.append(idx)
        return random.choice(answer)
