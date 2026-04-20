# test.py
# Deacon Steiner
# COSC 3020
# Lab11
# 20 April, 2026

from solution import move


def main():
    print(f" It takes {move([1, 0, 5])} move(s). Expect 3")  # Expect 3
    print(f"It takes {move([0, 3, 0])} move(s). Expect 2")  # Expect 2
    print(f"It takes {move([0, 2, 0])} move(s). Expect -1")  # Expect -1


if __name__ == "__main__":
    main()
