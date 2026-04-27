# test.py
# Deacon Steiner
# COSC 3020
# Lab12
# 27 April, 2026

from solution import payout, prob_dp, prob_rec


def main():
    print(
        f"Example 1: prob_rec(8, 6, 10) = {prob_rec(8, 6, 10)} (Player A wins 81.25% of the time)"
    )
    print(f"Example 2: prob_rec(9, 8, 10) = {prob_rec(9, 8, 10)}")
    print(f"Example 3: prob_rec(0, 0, 3) = {prob_rec(0, 0, 3)}")

    print("-" * 70)

    print(f"prob_dp(8, 6, 10) = {prob_dp(8, 6, 10)}")
    print(f"prob_dp(9, 8, 10) = {prob_dp(9, 8, 10)}")
    print(f"prob_dp(0, 0, 1) = {prob_dp(0, 0, 1)}")
    print(f"prob_dp(0, 0, 3) = {prob_dp(0, 0, 3)}")

    print("-" * 70)

    print(f"payout(8, 6, 10, 100) = {payout(8, 6, 10, 100)}")
    print(f"payout(9, 8, 10, 200) = {payout(9, 8, 10, 200)}")


if __name__ == "__main__":
    main()
