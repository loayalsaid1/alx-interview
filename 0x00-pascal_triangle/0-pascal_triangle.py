#!/usr/bin/python3
"""Module with one function to create a pascal tringle of a given height"""


def pascal_triangle(n):
    """Create a pascal trinagle with n rows

    Args:
            n: number of rows

    Return: a list of lists;


    Example:
    n = 5
    [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

            1
          1   1
        1   2   1
      1   3   3   1
    1   4   6   4   1

    Some observations:
    - each element starting from row 1 is sum of the 2 elemnts right above
    - The triangle is symmetric on y axis
    - Even rows have odd number of elements and vice versa
    - First and last elements are always 1 or course

    Let's go.
    """
    if n <= 0:
        return []

    # Hard code first 3 rows to save an if statement in each iteration next
    if n == 1:
        return [[1]]
    elif n == 2:
        return [[1], [1, 1]]
    elif n == 3:
        return [[1], [1, 1], [1, 2, 1]]

    # Now the juicy part!
    triangle = [[1], [1, 1], [1, 2, 1]]
    for i in range(3, n):
        row_num = i
        elements_count = row_num + 1
        # Add 1 at the beginning
        new_row = [1]
        # It's symmetric, so stop at the midle
        for j in range(1, elements_count // 2):
            new_element = \
                triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]
            new_row.append(new_element)

        # Now we are either in the midle #or one element
        # before if it's an even row
        first_half_copy = new_row.copy()

        # if this is an even row...(remember the observations?)..
        # then it has odd number of elements
        # so there is a middle number between the two identical wings
        if row_num % 2 == 0:
            middle_element = \
                triangle[row_num - 1][j] + triangle[row_num - 1][j + 1]
            new_row.append(middle_element)

        new_row += first_half_copy[::-1]

        triangle.append(new_row)

    return triangle
