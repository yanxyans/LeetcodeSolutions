import heapq

def min_cost_to_visit_every_node(graph: list[list[int]]) -> int:
    n = len(graph)
    min_cost = [float('inf') for _ in range(2 ** n)]
    min_cost[1] = 0
    heap = [(1, 0, 0)]
    while heap:
        bitmask, node, cost_to_visit = heapq.heappop(heap)
        if cost_to_visit > min_cost[bitmask]:
            continue

        for neighbor in range(n):
            if graph[node][neighbor] == 0:
                continue # edge does not exist

            bitmask_neighbor = bitmask | (1 << neighbor)
            if bitmask_neighbor != bitmask: # do not revisit previous node
                cost_neighbor = cost_to_visit + graph[node][neighbor]
                if cost_neighbor < min_cost[bitmask_neighbor]:
                    min_cost[bitmask_neighbor] = cost_neighbor
                    heapq.heappush(heap, (bitmask_neighbor, neighbor, cost_neighbor))

    return -1 if min_cost[2 ** n - 1] == float('inf') else min_cost[2 ** n - 1]

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