import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline
case = int(input())
graph = defaultdict(dict)
for _ in range(case):
    n, d, c = map(int, input().split())
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b] = graph[b].append({a : s})
        # print(a, b, s)
    print(graph)
    
def dijkstra(start):
    distances = {node: sys.maxsize for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, (distances[start], start))

    while queue:
        current_distance, node = heapq.heappop(queue)
        if distances[node] < current_distance:
            continue


        for adjacency_node, distance in graph[node].items():

            weighted_distance = current_distance + distance

            if weighted_distance < distances[adjacency_node]:

                distances[adjacency_node] = weighted_distance

                heapq.heappush(queue, (weighted_distance, adjacency_node))

    return distances

