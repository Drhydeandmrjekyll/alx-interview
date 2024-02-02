#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    """
    Determines if given data set represents valid UTF-8 encoding
    """
    bytes_remaining = 0

    for num in data:
        # Check if current byte is a continuation byte
        if bytes_remaining:
            if num >> 6 != 0b10:
                return False
            bytes_remaining -= 1
        else:
            # Count number of leading 1s to determine byte length
            if num >> 7 == 0b0:
                bytes_remaining = 0
            elif num >> 3 == 0b11110:
                bytes_remaining = 3
            elif num >> 4 == 0b1110:
                bytes_remaining = 2
            elif num >> 5 == 0b110:
                bytes_remaining = 1
            else:
                return False

    return bytes_remaining == 0
