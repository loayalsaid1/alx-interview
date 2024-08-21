#!/usr/bin/python3
"""Function to check the mimium operatiosn possible to multibly
 a number of chars to N, while you are starting with one char and
 you can only either copy all or paste
 """


def minOperations(n):
    """
    Function to check the mimium operatiosn possible to multibly
    a number of chars to N, while you are starting with one char and
    you can only either copy all or paste
    """

    if n <= 1:
        return 0

    copied_chars_count = 1
    chars_count = 2
    operations = 2

    while chars_count < n:
        """I'm thinking of another way to write this loop, but i'm not sure if
            the saved if statements will no make a difference sinse the loop
            will iterate more?
        """
        # Check if i need to spend an operation and copy all
        # by checking if doubling (copy all and paste) gets me more chars than
        # pasting twice
        if chars_count * 2 > chars_count + (2 * copied_chars_count):
            # Make sure that I actually need the double and
            # that pasting only once won't get me to target chars number
            if n - chars_count > copied_chars_count:
                copied_chars_count = chars_count
                operations += 1

        chars_count += copied_chars_count
        operations += 1
        # if n - chars_count <= copied_chars_count:
        # 	return operations + 1

        # if (chars_count + 2 * copied_chars_count) >= chars_count * 2:
        # 	chars_count += copied_chars_count
        # 	operations += 1
        # else:
        # 	copied_chars_count = chars_count
        # 	copied_chars_count *= 2
        # 	operations += 2

    return operations
