import heapq


class Solution:
    def lastStoneWeight(self, stones):
        # Convert all stone weights to negative and create a max-heap
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        # Continue until there is one or no stone left
        while len(max_heap) > 1:
            # Get the two heaviest stones (least negative)
            stone1 = heapq.heappop(max_heap)
            stone2 = heapq.heappop(max_heap)

            # If they are not equal, push the difference back into the heap
            if stone1 != stone2:
                heapq.heappush(max_heap, stone1 - stone2)

        # If there is a stone left, return its weight, otherwise return 0
        return -max_heap[0] if max_heap else 0



