#!/usr/bin/python3
"""Rodate 2d square matrix 90 degrees


    There is several solutions..
    I'm going with cycles. because it's easy to figure out and visualise.
    but abit tricky to actually code.

    Unlike transposing and reverse, which is very easy to implement..
    but took some time to discover the solution..

    you basically transpose it(make row into a columnd and vice versa)..
    where you actually, reverse it diagonally, loop over the length of it
    matrix and swap the positiosnin the row and in the column starting with
    point [i][i]

    and then treverse.. very easy to visualize too.
    but can be done with list comprehentions..

    anyways. i'm going with the tricky solution

    simply just go and visualize it with something like excalidraw..

    and as hints.. you make boundries.. top, bottom, left, and right.
    normally, horisontal and vertical will be the same as it's a square array

    and you make a cycle or replacing.. an outer shell and go one level deeper
    each time untill your right boundry touches your left boundry

    and yeah. this is the solution and following are the code. and I have
    no idea why I kept wringin all this...

    and one thing to tell.. Never see the solution before you are done thinking
    about it couple of times

    and never pass a solution untill you comprehended it.
"""


def rotate_2d_matrix(matrix):
    """Rotate 2d square matrix using cycles over layers of the matix"""
    left, right = 0, len(matrix) - 1

    while (left < right):
        for i in range(right - left):
            top, b = left, right
            top_left = matrix[top][left+i]
            matrix[top][left+i] = matrix[b-i][left]
            matrix[b-i][left] = matrix[b][right-i]
            matrix[b][right-i] = matrix[top+i][right]
            matrix[top+i][right] = top_left
        left += 1
        right -= 1
