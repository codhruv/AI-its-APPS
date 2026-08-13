from collections import deque  # Queue for BFS

# Graph as a dictionary
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

def bfs(start):
    visited = []            # Keep track of visited nodes
    queue = deque([start])  # Start with the first node in the queue

    while queue:  # Run until queue is empty
        node = queue.popleft()  # Take one node from queue

        if node not in visited:  # If not visited, process it
            print(node, end=" ")  # Print it
            visited.append(node)  # Mark it visited

            # Add all its neighbors to the queue
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

# Run BFS starting from 'A'
bfs('A')

#Output:
#A B C D E F
