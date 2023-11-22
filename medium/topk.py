class Solution(object):
    def topKFrequent(self, nums, k):
        frequency = {}
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        freq_list = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
        top_k_elements = [item[0] for item in freq_list[:k]]
        return top_k_elements
