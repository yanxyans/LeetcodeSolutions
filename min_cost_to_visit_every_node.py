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
            if graph[node][adj] != 0 and bitmask & (1 << adj) == 0:
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
    graph = [
        [0, 541, 246, 858, 384, 651, 494, 777, 711, 616],
        [863, 0, 497, 75, 0, 0, 531, 172, 667, 353],
        [254, 999, 0, 397, 54, 356, 77, 368, 349, 851],
        [927, 96, 291, 0, 272, 579, 0, 95, 361, 506],
        [266, 277, 264, 17, 0, 455, 472, 396, 211, 239],
        [797, 505, 405, 121, 104, 0, 566, 38, 369, 160],
        [379, 829, 719, 0, 477, 210, 0, 363, 481, 987],
        [270, 0, 779, 165, 260, 93, 446, 0, 850, 527],
        [995, 0, 99, 149, 696, 155, 882, 335, 0, 646],
        [502, 79, 766, 0, 7, 367, 832, 788, 605, 0]
    ]
    assert min_cost_to_visit_every_node(graph) == 1328