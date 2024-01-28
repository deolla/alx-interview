#!/usr/bin/python3
"""Log Parsing.
The script reads lines from stdin"""

from sys import stdin


try:
    code = {}
    total_size = 0
    for pop, line in enumerate(stdin, start=1):
        parts = line.split(" ")
        try:
            total_size += int(parts[-1])
            status = int(parts[-2])
            if status not in code:
                code[status] = 1
            else:
                code[status] += 1
        except (ValueError, IndexError):
            continue
        code = dict(sorted(code.items()))
        if pop % 10 == 0:
            print("File size: {}".format(total_size))
            for key, value in code.items():
                print("{}: {}".format(key, value))
except KeyboardInterrupt:
    pass
finally:
    print("File size: {}".format(total_size))
    for key, value in code.items():
        print("{}: {}".format(key, value))
