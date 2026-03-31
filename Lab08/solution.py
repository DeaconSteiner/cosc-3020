# solution.py
# Deacon Steiner
# COSC 3020
# Lab08
# 30 March, 2026

import heapq
from typing import Dict, List, Tuple


def signal_time(times: List[List[int]], n: int, k: int) -> int:
    graph = adjacency(times)
    pq = []
    dist = [float("inf")] * (n + 1)

    dist[k] = 0
    heapq.heappush(pq, (0, k))

    while pq:
        d, u = heapq.heappop(pq)

        if d > dist[u]:
            continue

        for v, w in graph.get(u, []):
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))

    res = max(dist[1:])
    return int(res) if res < float("inf") else -1


def adjacency(times: List[List[int]]) -> Dict[int, List[Tuple[int, int]]]:
    adj = {}

    for edge in times:
        src, dest, time = edge

        if src not in adj:
            adj[src] = []

        adj[src].append((dest, time))

    return adj
