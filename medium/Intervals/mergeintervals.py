def merge(intervals):
    # Step 1: Sort the intervals based on their start values
    intervals.sort(key=lambda x: x[0])

    # Step 2: Initialize an empty list for the result
    merged_intervals = []

    # Step 3: Iterate through the sorted intervals
    for interval in intervals:
        if not merged_intervals or interval[0] > merged_intervals[-1][1]:
            # If no overlap or the current interval starts after the last in result
            merged_intervals.append(interval)
        else:
            # If there is an overlap, merge the intervals by updating the end value
            merged_intervals[-1][1] = max(merged_intervals[-1][1], interval[1])

    return merged_intervals
