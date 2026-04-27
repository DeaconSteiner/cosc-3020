# solution.py
# Deacon Steiner
# COSC 3020
# Lab12
# 27 April, 2026

# P(a, b, n) = probability that Player A wins from state (a, b)
# = 1.0 if a == n (A already won)
# = 0.0 if b == n (B already won)
# = 0.5 * P(a+1, b, n) + 0.5 * P(a, b+1, n) otherwise


from typing import Tuple


def prob_rec(a: int, b: int, n: int) -> float:
    if a == n:
        return 1.0
    elif b == n:
        return 0.0
    else:
        return 0.5 * (prob_rec(a + 1, b, n) + prob_rec(a, b + 1, n))


def prob_dp(a: int, b: int, n: int) -> float:
    # Allocate a table dp of size (n+1) × (n+1)
    dp = [[0.0] * (n + 1) for _ in range(n + 1)]

    # Base Cases
    for j in range(n):
        dp[n][j] = 1.0
    for i in range(n):
        dp[i][n] = 0.0
    dp[n][n] = 1.0

    # Fill table
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            dp[i][j] = 0.5 * dp[i + 1][j] + 0.5 * dp[i][j + 1]

    # return dp[a][b]
    return dp[a][b]


def payout(a: int, b: int, n: int, pot: int) -> Tuple[float, float]:
    pA: float = prob_dp(a, b, n)
    share_A: float = round(pot * pA, 2)
    share_B: float = round(pot - share_A, 2)

    return (share_A, share_B)
