#!/usr/bin/python3
"""I have a bug in my original implementation..
 and i'm losing time for dealine.
let me do this nieve solution for now

i'm extremely tired today

remember,  teh error was, out of range index
there is a problem with turning when reaching a dead
end in the direction
"""

# def island_perimeter(grid):
#     found = False
#     for i in range(len(grid)):
#         for j in range(len(grid[0])):
#             if grid[i][j]:
#                 current_position = grid[i][j]
#                 found = True
#                 break
#         if found:
#             break

#     if not found:
#         return 0

#     count = 1
#     starting_point = current_position =  (i, j)

#     current_direction = "right"
#     next_search_direction = {'left': 'down','right': 'up', 'down': 'right',
#        'up': 'left'}
#     direction_change = {'down': (1, 0), 'up': (-1, 0), "right": (0, 1),
#        "left": (0, -1)}

#     def apply_direction_change(direction):
#         nonlocal direction_change
#         change = direction_change[direction]
#         return  (current_position[0] + change[0],
#    current_position[1] + change[1])

#     def get_value_at_position(position):
#         print(position)
#         if position[0] < 0 or position[1] < 0:
#             return 0
#         if position[0] == len(grid) or position[1] == len(grid[0]):
#             return 0
#         return grid[position[0]][position[1]]

#     while ((current_position == starting_point and
#         current_direction == 'up') is False):
#         next_direction = next_search_direction[current_direction]
#         next_search_position = apply_direction_change(next_direction)

#         if get_value_at_position(next_search_position) == 0:
#             count += 1
#             current_position =   apply_direction_change(current_direction)
#         else:
#             current_position = next_search_position
#             current_direction = next_direction

#     return count


def island_perimeter(grid):
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                # Check all four directions (up, down, left, right)
                if i == 0 or grid[i - 1][j] == 0:  # Up
                    perimeter += 1
                if i == rows - 1 or grid[i + 1][j] == 0:  # Down
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:  # Left
                    perimeter += 1
                if j == cols - 1 or grid[i][j + 1] == 0:  # Right
                    perimeter += 1

    return perimeter
