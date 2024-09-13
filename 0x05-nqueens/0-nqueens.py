#!/usr/bin/python3
"""A program to impelemnet a N-Queens problem

    Given an argument N, not less that 4

    return a list or lists each inner list represetn a position in the
    grid in on of the possible solutios
"""
import sys


def is_valid_position(row, column, previous_positions):
    """Aint the name describtive already?
    I'm too sleepy and I solved and brainsotrem this probelm early
    in the morning.. but forgot to write the code here
    so i'm not commenting anything

    My code, my github, Ok???????
    But it's easy  BTW"""
    for position in previous_positions:
        if (position[0] == row or
                position[1] == column or
                # Ok, just this one, This on is for diagnols.
                # # test it yourself and see
                abs(position[0] - row) == abs(position[1] - column)):
            return False

    return True


def solve(solutions, current_path, n, row):
    """Solves the N-Queens problem recursively
    I'm too sleepy and I solved and brainsotrem this probelm early
    in the morning.. but forgot to write the code here
    so i'm not commenting anything


    My code, my github, Ok???????
    But it's easy  BTW
    """
    if row >= n:
        solutions.append(current_path.copy())
        return

    for column in range(n):
        if is_valid_position(row, column, current_path):
            current_path.append([row, column])
            solve(solutions, current_path, n, row + 1)
            current_path.pop()

    return


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)

    if n < 4:
        print("N must be at least 4")
        exit(1)

    solutions = []
    solve(solutions, [], n, 0)

    for solution in solutions:
        print(solution)
