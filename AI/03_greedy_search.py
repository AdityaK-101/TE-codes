#Selection Sort greedy

def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


# Example
arr = [64, 25, 12, 22, 11]
print("Sorted:", selection_sort(arr))


# Dijkstra's Algorithm

import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]         
    
    while pq:
        curr_dist, curr_node = heapq.heappop(pq)
        
        if curr_dist > distances[curr_node]:
            continue
            
        for neighbor, weight in graph[curr_node]:
            distance = curr_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances


# Graph
graph = {
    'A': [('B', 4), ('C', 5)],
    'B': [('A', 4), ('C', 11), ('D', 9), ('E', 7)],
    'C': [('A', 5), ('B', 11), ('E', 3)],
    'D': [('B', 9), ('E', 13), ('F', 2)],
    'E': [('B', 7), ('C', 3), ('D', 13), ('F', 6)],
    'F': [('D', 2), ('E', 6)]
}

result = dijkstra(graph, 'A')

print("Shortest distances from A:")
for node, dist in result.items():
    print(f"  {node} : {dist}")


# Prim's Algorithm

import heapq

def mst_prim(graph, start):
    visited = set()
    min_heap = [(0, start)]       
    total_cost = 0
    mst_edges = []                

    while min_heap:
        cost, node = heapq.heappop(min_heap)
        
        if node in visited:
            continue
            
        visited.add(node)
        total_cost += cost

        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(min_heap, (weight, neighbor))

    print("Total nodes visited:", len(visited))
    print("Total Cost of MST:", total_cost)
    return total_cost


# Graph
graph = {
    1: [(2, 2), (4, 1), (5, 4)],
    2: [(1, 2), (3, 3), (4, 3), (6, 7)],
    3: [(2, 3), (4, 5), (6, 8)],
    4: [(1, 1), (2, 3), (3, 5), (5, 9)],
    5: [(1, 4), (4, 9)],
    6: [(2, 7), (3, 8)]
}

mst_prim(graph, 1)


# Kruskal's algo greedy

def find(parent, i):
    if parent[i] == i:
        return i
    return find(parent, parent[i])


def union(parent, x, y):
    parent[find(parent, x)] = find(parent, y)


def kruskal(vertices, edges):
    edges = sorted(edges, key=lambda x: x[2])

    parent = {v: v for v in vertices}
    mst = []
    total_cost = 0

    for u, v, w in edges:

        if find(parent, u) != find(parent, v):
            union(parent, u, v)
            mst.append((u, v, w))
            total_cost += w  

    print("MST Edges:", mst)
    print("Total Cost of MST:", total_cost) 
    return mst


# Graph
vertices = [0, 1, 2, 3, 4, 5, 6, 7, 8]

edges = [
    (0, 1, 4), (0, 7, 8), (1, 2, 8), (1, 7, 11),
    (2, 3, 7), (2, 8, 2), (2, 5, 4), (3, 4, 9),
    (3, 5, 14), (4, 5, 10), (5, 6, 2), (6, 7, 1),
    (6, 8, 6), (7, 8, 7)
]

kruskal(vertices, edges)