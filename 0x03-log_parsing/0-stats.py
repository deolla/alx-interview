#!/usr/bin/python3
"""Write a script that reads stdin line by line and computes metrics"""
import sys
import signal


if __name__ == "__main__":
    status_codes = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0,
    }
    file_size = 0
    counter = 0

    def print_stats():
        """Prints the accumulated metrics"""
        print("File size: {}".format(file_size))
        for key, value in sorted(status_codes.items()):
            if value != 0:
                print("{}: {}".format(key, value))

    try:
        for line in sys.stdin:
            counter += 1
            data = line.split()
            try:
                status = data[-2]
                file_size += int(data[-1])
                if status in status_codes:
                    status_codes[status] += 1
            except BaseException:
                pass
            if counter % 10 == 0:
                print_stats()
    except KeyboardInterrupt:
        print_stats()
        raise
    print_stats()
