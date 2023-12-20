#!/usr/bin/python3

import sys


def status_msg(dict, size):
    """
    Total file size: size
    size is the sum of previous file size
    dict is the status
    Returns:
        Nothing
    """

    print("File size: {}".format(size))
    for key, value in sorted(dict.items()):
        if value != 0:
            print("{}: {}".format(key, value))


size = 0
coder = 0
counter = 0
dict = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

try:
    for line in sys.stdin:
        parsed_line = line.split()
        parsed_line = parsed_line[::-1]


        if len(parsed_line) > 2:
            counter += 1

            if counter <= 10:
                size += int(parsed_line[0])
                coder = parsed_line[1]

                if (coder in dict.keys()):
                    dict[coder] += 1

            if (counter == 10):
                status_msg(dict, size)
                counter = 0

finally:
    status_msg(dict, size)
