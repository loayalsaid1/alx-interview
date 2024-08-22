#!/usr/bin/python3
"""
        1- Intuitively, if the point was to reach n or more,
    you can think of a greedy algorithm.

    while chars_count < n:
        if doubling (copy all then paste) will give you more than 2 paste
        operations,
            do it
            double ops number
        otherwise:
            paste once
            add one
    return operations

    But, you have to reach exactly N, so you need to be precise about where
    you will copy because you will only multiply. You can't paste just
    portions of what you have in memory.

    What you can do is keep dividing n by the smallest number possible because
    you know that if the smaller the divisor, the smaller the multiplications
    you have to make to get it.

    And if you note, if you have 4 chars, to make it reach 12,
    12 / 4 is 3, so you have to multiply by 3, which is, to copy all and
    paste twice, (copy => 4, paste => 8, paste => 12). So, multiplication by
    a factor takes <factor> operations.

    And if you have 12, and you wanna be efficient, you have to divide it by
    the smallest possible number, here for example 2, and you will get 6.

    So you have to get 6 the most efficient way, and to make it 12, you can
    only spend 2 ops: 1 copy and the rest is only 1 paste.

    And then repeat with 6, get it the most efficient way.

    And remember, you want to get only N, and that you can only make a full
    paste, not only a portion of it, or paste then delete.

    We have to make sure that when we copy, we are copying in a place that the
    current count, when multiplied, takes us to the number we want.

    That's why we take it from the top, n, divide as less as possible, and
    keep trying this with the rest of the numbers. Get them as efficiently as
    possible until we reach 1, and then we are done.

    This is very efficient. You may do backtracking, the same with the greedy
    one above, and then if you pass <n> in your tree and not <n> exactly,
    then this one fails and so on.

    Now, with this, it may be clear to you, either from the side of solving
    this problem or another problem, which is actually step-by-step building
    the actual text.

    Also, something crossing my mind is that you may, just like me, get a bit
    confused by the problem because you are thinking about the process of
    building. So you are both looking at it from the top, which is from N
    down to 1 and factorization and stuff, and at the same time from the
    bottom, when you are actually building the text, and copying and pasting
    and when to stop, etc.

    Me too, my head is very messy right now, and reaching this point actually
    was hard on me.

    I don't know who I'm talking to.

    I noticed a pattern with an example. Say n = 100. You will get factoring
    like this: 2 2 5 5,... 100 / 2 => 50 / 2 => 25 / 5 => 5 => 5 = 1.

    And when you are building, you can get 5 5 2 2 or the opposite.
    You can either copy at 2, then times 2 (4), then times 5 (20),
    then times 5 (100), or the opposite, like 5 5 2 2.

    It's the same result of text and will end up with the same value, of
    course, and the same number of steps.

    For the reverse, that can be that multiplication is interchangeable.
    For the equality of value, that can be—or in fact, it is—we said each
    factor will give <factor> operations.
"""


def minOperations(n):
    """
    Fewest number of operations to double 1 characters to <n> characters if
    you can only use the two operations; Copy All and Paste
    """
    if type(n) is not int or n <= 1:
        return 0

    # starting at 1 character, no operations done
    operations = 0

    # starting deviding wiht least possible
    factor = 2

    while n > 1:
        # Keep deviding with least possible
        while n % factor == 0:
            # devide by the factor and check next keep with next value
            n /= factor
            # check if you have 3 chars and want to get to 9, 3 * 3 = 9
            operations += factor

        # You can jump directly to next prime
        # but let's not take more processing
        factor += 1

    return operations
