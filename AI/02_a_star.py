# For graph

import heapq

graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('E', 1)],
    'C': [('F', 5)],
    'E': [('F', 2)],
    'F': []
}

heuristic = {
    'A': 6,
    'B': 4,
    'C': 2,
    'E': 1,
    'F': 0
}


def astar(start, goal):
    pq = [(0, start)]
    g = {start: 0}
    parent = {start: None}

    while pq:
        f, node = heapq.heappop(pq)
        if node == goal:
            path = []
            while node:
                path.append(node)
                node = parent[node]
            return path[::-1], g[goal]

        for neigh, cost in graph[node]:
            new_g = g[node] + cost
            if neigh not in g or new_g < g[neigh]:
                g[neigh] = new_g
                f = new_g + heuristic[neigh]
                heapq.heappush(pq, (f, neigh))
                parent[neigh] = node

print(astar('A', 'F'))

# For 8 puzzle game

import heapq

GOAL_STATE = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 0)
)

MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def misplaced_tiles(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != GOAL_STATE[i][j]:
                count = count + 1
    return count


def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j


def get_neighbors(state):
    neighbors = []
    x, y = find_blank(state)

    for dx, dy in MOVES:
        nx, ny = x + dx, y + dy

        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [list(row) for row in state]

            new_state[x][y], new_state[nx][ny] = (
                new_state[nx][ny],
                new_state[x][y]
            )

            neighbors.append(tuple(tuple(row) for row in new_state))

    return neighbors


def a_star(start_state):
    pq = []

    heapq.heappush(
        pq,
        (misplaced_tiles(start_state), 0, start_state, [])
    )

    visited = set()

    while pq:
        f, g, current, path = heapq.heappop(pq)

        if current == GOAL_STATE:
            return path + [current]

        if current in visited:
            continue

        visited.add(current)

        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                new_g = g + 1
                new_h = misplaced_tiles(neighbor)

                heapq.heappush(
                    pq,
                    (
                        new_g + new_h,
                        new_g,
                        neighbor,
                        path + [current]
                    )
                )

    return None


start_state = (
    (1, 2, 3),
    (4, 0, 6),
    (7, 5, 8)
)

solution = a_star(start_state)

if solution:
    print("Solution found in", len(solution) - 1, "moves:")

    for step in solution:
        for row in step:
            print(row)
        print()

else:
    print("No solution")