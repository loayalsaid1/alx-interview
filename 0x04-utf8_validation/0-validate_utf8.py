#!/usr/bin/python3
"""a functin to validate a set of data to be UTF-8 compatible

    Data will be represented in the form of list of integers.
    Each represents a byte.
"""


def validUTF8(data):
    """Validate a set of bytes represented by integers to
        be UTF-8 valid encoding

        Args:
            data: A list of integers, each representing a
                byte
    """
    def get_last_byte(number):
        return number & 0b11111111

    if type(data) is not list:
        return False

    i = 0
    while i < len(data):
        byte = get_last_byte(data[i])

        # check if byte is has 0 at last bit; 0xxx xxxx
        # meaning it representig a valid single byte codepoint
        if byte < 0b10000000:
            i += 1
            continue
        else:
            remaining_bits = 0

            last_5_bits = byte >> 3

            if last_5_bits == 0b11110:
                remaining_bits = 3
            elif last_5_bits & 0b11110 == 0b11100:
                remaining_bits = 2
            elif last_5_bits & 0b11100 == 0b11000:
                remaining_bits = 1
            else:
                return False

            i += 1
            while remaining_bits and i < len(data):
                if get_last_byte(data[i]) >> 6 != 0b10:
                    return False
                remaining_bits -= 1
                i += 1
            if remaining_bits != 0 and i >= len(data):
                return False

    # Now we ran out of bytes without a failure, but are we still
    # In the middle of a character?
    return True
