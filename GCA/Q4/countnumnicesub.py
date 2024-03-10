class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def countAtMostK(odds, k):
            left = result = 0
            for right in range(len(odds)):
                k -= odds[right] % 2  # Decrease k for each odd
                while k < 0:
                    # Move left pointer if we exceeded k odds
                    k += odds[left] % 2
                    left += 1
                result += right - left + 1  # Count subarrays
            return result

        # Count subarrays with at most k odds and subtract those with at most (k-1) odds
        return countAtMostK(nums, k) - countAtMostK(nums, k-1)
