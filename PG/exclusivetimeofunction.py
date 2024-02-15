class Solution(object):
    def exclusiveTime(self, n, logs):
        stack = []  # To keep track of function calls
        # Initialize the result array to store exclusive times
        result = [0] * n

        for log in logs:
            fid, event, time = log.split(':')
            fid, time = int(fid), int(time)

            if event == "start":
                if stack:
                    # Update the exclusive time for the function at the stack's top
                    result[stack[-1][0]] += time - stack[-1][1]
                    # Update the start time to the current time
                    stack[-1][1] = time
                # Push the new function call onto the stack
                stack.append([fid, time])
            else:
                # Pop the function call from the stack and update its exclusive time
                _, start_time = stack.pop()
                duration = time - start_time + 1  # Include the 'end' timestamp
                result[fid] += duration

                if stack:
                    # Update the start time for the next function on the stack
                    stack[-1][1] = time + 1

        return result

    def exclusiveTime_v2(self, n, logs):
        stack = []
        result = [0] * n

        def normalizeProcessTime(processTime):
            return processTime.encode('ascii', 'ignore').split(':')

        for processTime in logs:
            processId, eventType, time = normalizeProcessTime(processTime)

            if eventType == "start":
                stack.append([processId, time])

            elif eventType == "end":
                processId, startTime = stack.pop()
                timeSpent = int(time) - int(startTime) + 1
                result[int(processId)] += timeSpent

                # Decrement time for next process in the stack
                if len(stack) != 0:
                    nextProcessId, timeSpentByNextProcess = stack[-1]
                    result[int(nextProcessId)] -= timeSpent

        return result
