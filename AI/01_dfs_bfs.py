graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# DFS (Recursive)
def dfs(node, visited):

    if node not in visited:
        print(node, end=" ")

        visited.add(node)

        for neighbor in graph[node]:
            dfs(neighbor, visited)


# BFS (Recursive)
from collections import deque

def bfs(queue, visited):

    if not queue:
        return

    node = queue.popleft()

    print(node, end=" ")

    for neighbor in graph[node]:

        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)

    bfs(queue, visited)


print("DFS:")
dfs('A', set())

print("\nBFS:")

visited = set(['A'])
queue = deque(['A'])

bfs(queue, visited)