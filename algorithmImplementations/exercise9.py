from collections import deque

vertices = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
edges = [(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (3, 1), (3, 2), (4, 1), (4, 5), (4, 8), (5, 4), (5, 6), (5, 7), (6, 5), (6, 7), (6, 8), (6, 9), (7, 5), (7, 6), (8, 4), (8, 6), (8, 9), (9, 6), (9, 8), (9, 10), (10, 9)]

def pathToDest(vertices, edges):
    visited = set()
    queue = deque(edges) # Source at 1 (vertices[0])
    visited.add(vertices[0])
    orderAccessed = []

    for i in range (len(queue)):
        curNode = queue.popleft()
        orderAccessed.append(curNode)

        for neighbor in edges[curNode]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
    return orderAccessed



print(pathToDest(vertices, edges))