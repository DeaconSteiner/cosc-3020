from solution import can_meet

interval1 = [[0, 30], [5, 10], [15, 20]]
interval2 = [[7, 10], [2, 4]]


def main():
    print(
        f"for the meeting times {interval1}, can you attend all meetings? {can_meet(interval1)}"
    )
    print(
        f"for the meeting times {interval2}, can you attend all meetings? {can_meet(interval2)}"
    )


if __name__ == "__main__":
    main()
