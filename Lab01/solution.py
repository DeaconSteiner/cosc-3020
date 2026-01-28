def can_meet(interval):
    interval.sort(key=lambda x: x[0])

    prev = interval[0]
    for meeting in interval[1:]:
        current = meeting
        if current[0] < prev[1]:
            return False
        prev = current
    return True
