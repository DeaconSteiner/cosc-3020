# test.py
# Deacon Steiner
# COSC 3020
# Lab10
# 13 April, 2026

from solution import removeStones


def main():
    print(
        f"You can remove {removeStones([[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]])} stones from the group: [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]"
    )

    print(
        f"You can remove {removeStones([[0, 0], [0, 2], [1, 1], [2, 0], [2, 2]])} from the group: [[0,0],[0,2],[1,1],[2,0],[2,2]]"
    )

    print(f"You can remove {removeStones([[0, 0]])} stones from the group: [[0,0]]")


if __name__ == "__main__":
    main()
