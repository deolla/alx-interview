#!/usr/bin/env python3
"""A method that determines if a given data set
represents a valid UTF-8 encoding"""


def validUTF8(data):
    """Return: True if data is a valid UTF-8 encoding, else return False."""
    bytes = 0

    for i in range(len(data)):
        byte = data[i] & 0xFF
        if bytes == 0:
            if byte >> 5 == 0b110:
                bytes = 1
            elif byte >> 4 == 0b1110:
                bytes = 2
            elif byte >> 3 == 0b11110:
                bytes = 3
            elif byte >> 7 == 1:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            bytes -= 1
    return bytes == 0
