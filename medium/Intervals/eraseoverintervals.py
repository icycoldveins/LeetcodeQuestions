class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        # Step 1: Sort the intervals based on end points
        intervals.sort(key=lambda x: x[1])

        # Step 2: Initialize variables
        count = 0  # Number of intervals to remove
        end = intervals[0][1]  # End point of the first interval

        # Step 3: Iterate through the sorted intervals
        for i in range(1, len(intervals)):
            current_start, current_end = intervals[i]

            # Check if the current interval overlaps with the previous one
            if current_start < end:
                count += 1  # Increment count to remove the overlapping interval
            else:
                end = current_end  # Update end to the end of the current interval

        # Step 4: Return the count of intervals to remove
        return count
