#!/usr/bin/python3
""" this script holds a function for creating
""" pascals triangle


def pascal_triangle(n):
    """
    this function returns a list
    """

    if n <= 0:
        return []

    answer = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(answer[i - 1][j - 1] + answer[i - 1][j])
        row.append(1)
        answer.append(row)
    return answer
