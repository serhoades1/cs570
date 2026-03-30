tempList = [5, 7, 7, 8, 8, 10]
start = tempList[0]
mid = len(tempList) / 2
end = len(tempList) - 1
endList = []
target = 8

def targetLoc(start, mid): # binary search tree to find at least one target element in the list
    while start != end:
        if tempList[mid] > target:
            end = mid
            mid = start + ((end - start) / 2)
            targetLoc(start, end)
        if tempList[mid] < target:
            start = mid
            mid = start + ((end - start) / 2)
            targetLoc(start, end)
        if tempList[mid] == target:
            secondList = [tempList[start], tempList[end]]
            endList.append(findExtremes()) # calls second function to continue
            break

def findExtremes(secondList[]):
    while start != end: # second BST to find the leftmost and rightmost targets
        if secondList[mid] > target:

            return
        if secondList[mid] == target:
            start = mid
            mid = start + ((end - start) / 2)
            findExtremes(start, end)
            endList.append(mid)
            return 

    return endList
# third BST to find rightost element

print(targetLoc(start, mid))
