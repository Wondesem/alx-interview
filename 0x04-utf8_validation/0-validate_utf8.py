#!/usr/bin/python3
"""UTF-8 Validation"""


def validUTF8(data):
    """Determines if a given data set
    represents a valid utf-8 encoding
    """
    number_bytes = 0

    binari_1 = 1 << 7
    binari_2 = 1 << 6

    for i in data:

        byte_asci = 1 << 7

        if number_bytes == 0:

            while byte_asci & i:
                number_bytes += 1
                byte_asci = byte_asci >> 1

            if number_bytes == 0:
                continue

            if number_bytes == 1 or number_bytes > 4:
                return False

        else:
            if not (i & binari_1 and not (i & binari_2)):
                return False

        number_bytes -= 1

    if number_bytes == 0:
        return True

    return False
