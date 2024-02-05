class Solution:
    def can_attend_meetings(self, intervals):
        if not intervals:
            return True  # No intervals to conflict

        # Step 1: Sorting by start times
        intervals.sort(key=lambda x: x[0])

        # Step 2: Tracking Overlaps
        end_times = [interval[1] for interval in intervals]
        j = 0

        for i in range(1, len(intervals)):
            if intervals[i][0] < end_times[j]:
                return False  # Conflict found
            j += 1

        return True  # No conflicts found, can attend all meetings
        