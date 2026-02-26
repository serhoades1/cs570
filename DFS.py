def execute_dfs(n, edges, start_vertex):
    # Size n + 1 used so we can ignore index 0 and start from 1
    visited = [0] * (n + 1)
    parent = [-1] * (n + 1)
    pre = [-1] * (n + 1)
    post = [-1] * (n + 1)
    
    count = 0
    
    # Convert edge list to an adjacency list for O(V+E) lookup
    # Represents "for each (i, j) in E"
    adj = {i: [] for i in range(1, n + 1)}
    for u, v in edges:
        adj[u].append(v)
        
    def dfs(i):
        nonlocal count # Allows us to modify the count variable from the outer scope
        
        # Mark i as visited and record pre-order time
        visited[i] = 1
        pre[i] = count
        count += 1
        
        # Explore each neighbor of i recursively
        for j in adj[i]:
            if visited[j] == 0:
                parent[j] = i
                dfs(j)
                
        # Record post-order time
        post[i] = count
        count += 1

    # Execution
    dfs(start_vertex)
    
    return visited, parent, pre, post

# Graph with 6 vertices
num_vertices = 6
# Edges: 1->2, 1->3, 2->4, 2->5, 3->6, 5->6
edge_list = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (5, 6)]

visited_arr, parent_arr, pre_arr, post_arr = execute_dfs(num_vertices, edge_list, 1)

print("Vertex | Visited | Parent | Pre (Count) | Post (Count)")
print("-" * 55)
for v in range(1, num_vertices + 1):
    print(f"   {v}   |    {visited_arr[v]}    |   {parent_arr[v]:>2}   |      {pre_arr[v]:>2}     |      {post_arr[v]:>2}")