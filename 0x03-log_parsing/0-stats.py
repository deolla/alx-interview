#!/usr/bin/python3
"""log parsing"""
import sys


def print_stats(total_size, status_codes):
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))


def main():
    total_size = 0
    status_codes = {}

    try:
        for i, line in enumerate(sys.stdin, 1):
            try:
                parts = line.split()
                ip, date, method, path, version, status_code, file_size = parts[:7]
                file_size = int(file_size)
            except (ValueError, IndexError):
                # Skip invalid lines
                continue

            total_size += file_size
            status_codes[status_code] = status_codes.get(status_code, 0) + 1

            if i % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        pass  # Continue to print final stats even if interrupted

    print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()
