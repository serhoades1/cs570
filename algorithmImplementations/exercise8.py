from collections import deque

rows = 3
columns = 2
# edges = [[0, 1], [1, 2], [2, 0]]
edges = [[0, 1], [1, 2], [3, 1]]
# edges = [[0 for j in range(columns)] for i in range(rows)]
visited = set()

source = 0
destination = 3

def validPath(edges, source, destination):
    for i in range(len(edges)):
        for j in range(len(edges[i])):
            visited.add(edges[i][j])
    if source in visited and destination in visited:
        return True
    return False

print(validPath(edges, source, destination))