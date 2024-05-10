class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        fracs = []

        for i in range(len(arr) - 1):
            for j in range(i + 1, len(arr)):
                fracs.append([arr[i], arr[j]])

        fracs.sort(key=lambda x: x[0]/x[1])

        return fracs[k-1]
