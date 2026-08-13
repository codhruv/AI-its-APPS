# Graph as a dictionary
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = []  # Keep track of visited nodes

def dfs(node):
    if node not in visited:        # If not visited yet
        print(node, end=" ")       # Print the node
        visited.append(node)       # Mark as visited

        # Visit all neighbors one by one
        for neighbor in graph[node]:
            dfs(neighbor)

# Run DFS starting from 'A'
dfs('A')

#Output:
#A B D E F C
