class Solution(object):
    def insert(self, intervals, newInterval):
        result = []
        i = 0

        # Iterate through existing intervals to find the correct position for the newInterval
        while i < len(intervals):  # Fixed syntax error here (removed extraneous '=')
            start, end = intervals[i]

            # If the newInterval ends before the current interval starts, there is no overlap
            if newInterval[1] < start:
                result.append(newInterval)
                # Since newInterval is added, append the remaining intervals and return the result
                return result + intervals[i:]

            # If the current interval ends before the newInterval starts, there is no overlap
            elif end < newInterval[0]:
                result.append(intervals[i])
                i += 1  # Move to the next interval

            # Overlapping intervals are merged
            else:
                # Update newInterval to be the merger of it and the overlapping interval
                newInterval = [min(start, newInterval[0]),
                               max(end, newInterval[1])]
                i += 1  # Continue to check for more overlaps

        # After processing all intervals, add the final newInterval to the result
        result.append(newInterval)

        return result
