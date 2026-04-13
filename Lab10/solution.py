# solution.py
# Deacon Steiner
# COSC 3020
# Lab10
# 13 April, 2026

from typing import List


def removeStones(stones: List[List[int]]) -> int:
    stoneLen = len(stones)
    PR = empty_partition()

    for i in range(stoneLen):
        makeset(PR, i)

    for i in range(stoneLen):
        for j in range(stoneLen):
            if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                union(PR, i, j)

    roots = set()
    for i in range(stoneLen):
        roots.add(find(PR, i))

    components = len(roots)
    return stoneLen - components


def empty_partition():
    return ({}, {})


def makeset(PR, u):
    P, R = PR
    P[u] = u
    R[u] = 0


def find(PR, u):
    P, R = PR
    if P[u] != u:
        P[u] = find(PR, P[u])
    return P[u]


def union(PR, u, v):
    P, R = PR
    p_u = find(PR, u)
    p_v = find(PR, v)
    if p_u == p_v:
        return
    if R[p_u] > R[p_v]:
        P[p_v] = p_u
    else:
        P[p_u] = p_v
        if R[p_u] == R[p_v]:
            R[p_v] = R[p_v] + 1
