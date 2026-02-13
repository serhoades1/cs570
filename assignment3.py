def maxSquare(n, m, hBars, vBars):
    if (n == 0 and m == 0) or len(hBars) == 0 or len(vBars) == 0:
        return 1

    hMax = 1
    vMax = 1
    consecutiveStreak = 1
        
    for i in range (1, len(hBars)):
        if hBars[i] == hBars[i-1] + 1:
            consecutiveStreak += 1
        else:
            consecutiveStreak = 1
        hMax = max(hMax, consecutiveStreak)

    consecutiveStreak = 1

    for i in range (1, len(vBars)):
        if vBars[i] == vBars[i-1] + 1:
            consecutiveStreak += 1
        else:
            consecutiveStreak = 1
        vMax = max(vMax, consecutiveStreak)

    hMax += 1
    vMax += 1

    if hMax < vMax:
        maxArea = hMax * hMax
    else:
        maxArea = vMax * vMax


    return maxArea

# n = 2
# m = 1
# hBars = [2, 3]
# vBars = [2]

# n = 1
# m = 2
# hBars = [2]
# vBars = [2]

# n = 2
# m = 3
# hBars = [2, 3]
# vBars = [2, 4]

n = 6
m = 8
hBars = [2, 3, 6, 7, 8, 9]
vBars = [2, 4, 5, 6, 7]




print(maxSquare(n, m, hBars, vBars))