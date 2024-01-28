#!/usr/bin/python3
"""Log parsing module"""
import sys

from sys import stdin

try:
    codes = {}
    total_size = 0
    for i, line in enumerate(stdin, start=1):
        parts = line.split(" ")
        try:
            total_size += int(parts[-1])
            status = int(parts[-2])
            if status not in codes:
                codes[status] = 1
            else:
                codes[status] += 1
        except (ValueError, IndexError):
            continue

        if i % 10 == 0:
            print("File size: {}".format(total_size))
            for key, val in sorted(codes.items()):
                print("{}: {}".format(key, val))

except KeyboardInterrupt:
    pass

finally:
    print("File size: {}".format(total_size))
    for key, val in sorted(codes.items()):
        print("{}: {}".format(key, val))
