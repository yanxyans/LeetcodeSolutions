from collections import deque

def min_cost_to_visit_every_node(graph: list[list[int]]) -> int:
    n = len(graph)
    dp = {(1, 0): 0}
    queue = deque([(1, 0, 0)])

    while queue:
        bitmask, node, cost = queue.popleft()
        if cost > dp[(bitmask, node)]:
            continue

        for adj in range(n):
            if graph[node][adj] != 0:
                cost_to_adj = cost + graph[node][adj]
                bitmask_adj = bitmask | (1 << adj)
                if (bitmask_adj, adj) not in dp or dp[(bitmask_adj, adj)] > cost_to_adj:
                    dp[(bitmask_adj, adj)] = cost_to_adj
                    queue.append((bitmask_adj, adj, cost_to_adj))

    min_cost = float('inf')
    all_visited = (1 << n) - 1
    for node in range(n):
        if (all_visited, node) in dp:
            min_cost = min(min_cost, dp[(all_visited, node)])
    return -1 if min_cost == float('inf') else min_cost

if __name__ == '__main__':
    assert min_cost_to_visit_every_node([[0, 2], [2, 0]]) == 2
    assert min_cost_to_visit_every_node([
        [0, 100, 100, 1],
        [0, 0, 100, 0],
        [0, 1, 0, 0],
        [0, 20, 1, 0]]) == 3
    assert min_cost_to_visit_every_node([
        [0, 0, 1],
        [0, 0, 0],
        [0, 2, 0]]) == 3
    assert min_cost_to_visit_every_node([
        [0, 2, 2, 1, 2],
        [2, 0, 2, 2, 1],
        [2, 1, 0, 2, 2],
        [2, 2, 1, 0, 2],
        [2, 2, 2, 2, 0]]) == 4