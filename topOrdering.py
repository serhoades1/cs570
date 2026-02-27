def topological_order_with_longest_path(A):

    n = len(A)
    
    # Initialize indegree and Longest Path To (LPT) arrays
    indegree = [0] * n
    LPT = [0] * n
    topological_order = []

    # Calculate initial in-degrees for all nodes
    for i in range(n):
        for j in range(n):
            indegree[i] += A[j][i]

    # Process nodes to find topological order and longest paths
    for i in range(n):
        
        # Choose j with indegree[j] == 0
        j = -1
        for idx in range(n):
            if indegree[idx] == 0:
                j = idx
                break
                
        # If no node has indegree 0, the graph is not a DAG (contains a cycle)
        if j == -1:
            raise ValueError("Graph contains a cycle, topological sort not possible.")

        # Enumerate j (add to output list)
        topological_order.append(j)
        
        # Mark j as visited by setting its indegree to -1
        indegree[j] = -1

        # Update neighbors of j
        for k in range(n):
            if A[j][k] == 1:
                indegree[k] -= 1
                LPT[k] = max(LPT[k], 1 + LPT[j])

    return topological_order, LPT


if __name__ == "__main__":
    # Adjacency Matrix
    # 0 -> 1
    # 0 -> 2
    # 1 -> 2
    # 1 -> 3
    # 2 -> 3
    
    graph_matrix = [
        [0, 1, 1, 0], # Node 0
        [0, 0, 1, 1], # Node 1
        [0, 0, 0, 1], # Node 2
        [0, 0, 0, 0] # Node 3
    ]

    order, longest_paths = topological_order_with_longest_path(graph_matrix)

    print(f"Topological Order: {order}")
    print(f"Longest Path to each node (LPT): {longest_paths}")