intervals = [[1, 4], [2, 6], [8, 10]]
# intervals = [[2, 4], [6, 9], [1, 2]]
sortedIntervals = sorted(intervals)
newIntervals = []

def intervalOverlap(sortedIntervals):
    smallInterval = []
    for i in range(len(sortedIntervals) - 1):
        for j in range(len(sortedIntervals[i]) - 1):
            if sortedIntervals[i][j + 1] >= sortedIntervals[i + 1][j]:
                smallInterval = [sortedIntervals[i][j], sortedIntervals[i + 1][j + 1]]
                newIntervals.append(smallInterval) # First value from first array and second from second
                continue # Needs to skip 2 arrays before going again
            elif sortedIntervals[i][j] <= sortedIntervals[i - 1][j + 1]:
                continue
            else:
                newIntervals.append(sortedIntervals[i])
    newIntervals.append(sortedIntervals[len(sortedIntervals) - 1])
    return newIntervals

print(intervalOverlap(sortedIntervals))
