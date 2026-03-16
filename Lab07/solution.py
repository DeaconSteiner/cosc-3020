# solution.py
# Deacon Steiner
# COSC 3020
# Lab07
# 15 March, 2026


def dfsRec(rooms, visited, curr):
    visited[curr] = True

    for key in rooms[curr]:
        if not visited[key]:
            dfsRec(rooms, visited, key)


def dfs(rooms):
    visited = [False] * len(rooms)
    dfsRec(rooms, visited, 0)
    return all(visited)


def main():
    rooms1 = [[1], [2], [3], []]
    print(f"Can all rooms in room set 1, {rooms1}, be reached? {dfs(rooms1)}")

    rooms2 = [[1, 3], [3, 0, 1], [2], [0]]
    print(f"Can all rooms in room set 2, {rooms2}, be reached? {dfs(rooms2)}")


if __name__ == "__main__":
    main()
