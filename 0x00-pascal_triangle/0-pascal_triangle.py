#!/usr/bin/python3
# this script holds a function for creating
# pascals triangle

def pascal_triangle(n):
    """
    this function returns a list
    """

    answer = []
    answer1 = [[1]]
    answer2 = [[1], [1, 1]]
    final = answer2.copy()

    if n <= 0:
        return answer

    elif n == 1:
        return answer1

    elif n == 2:
        return answer2
    
    elif n > 2:
        for i in range(2, n):
            mid = final[-1]
            for j in mid:
                if j == 1 and j == mid[0]:

            

