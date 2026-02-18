def get_top_n_marks(marks: list, n: int) -> list:
    if not isinstance(marks, list):
        raise TypeError("marks must be a list")

    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    sorted_marks = sorted(marks, reverse=True)
    return sorted_marks[:n]


def count_mark_occurrence(marks: list, value: int) -> int:
    if not isinstance(marks, list):
        raise TypeError("marks must be a list")

    return marks.count(value)


def get_high_scorers(marks: list, threshold: int) -> list:
    if not isinstance(marks, list):
        raise TypeError("marks must be a list")

    return [mark for mark in marks if mark >= threshold]
