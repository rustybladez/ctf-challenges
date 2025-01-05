from collections import defaultdict, deque

def build_tree(edges):
    """
    Build an adjacency list representation of the tree.
    """
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    return graph

def calculate_distances(graph, start):
    """
    Use BFS to calculate distances from the starting node to all other nodes.
    """
    distances = {}
    queue = deque([(start, 0)])
    while queue:
        node, dist = queue.popleft()
        if node in distances:
            continue
        distances[node] = dist
        for neighbor in graph[node]:
            if neighbor not in distances:
                queue.append((neighbor, dist + 1))
    return distances

def find_burn_points(graph, n):
    """
    Find optimal burn points to minimize the maximum burning time.
    """
    max_dist = float('inf')
    best_knot = None

    for knot in range(1, n + 1):
        distances = calculate_distances(graph, knot)
        furthest = max(distances.values())
        if furthest < max_dist:
            max_dist = furthest
            best_knot = knot

    # Burn the best knot at time 0
    return [(best_knot, 0)]

def solve_challenge(num_knots, edges):
    """
    Solve the challenge for the given number of knots and edges.
    """
    graph = build_tree(edges)
    burn_points = find_burn_points(graph, num_knots)
    # Format the result as expected
    result = f"{len(burn_points)} " + " ".join(f"{knot} {time}" for knot, time in burn_points)
    return result

# Input for the challenge
num_knots = 10
edges = [
    (1, 6),
    (1, 9),
    (9, 3),
    (3, 7),
    (3, 10),
    (10, 4),
    (10, 2),
    (3, 8),
    (9, 5)
]

# Solve the challenge and print the result
output = solve_challenge(num_knots, edges)
print(f"Enter the number of knots you want to burn as {output}")
