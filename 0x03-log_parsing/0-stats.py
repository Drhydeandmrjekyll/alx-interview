#!/usr/bin/python3
"""
Log Parsing Script - Reads stdin, computes metrics, and prints statistics.
"""

import sys


def print_stats(total_size, status_codes):
    """
    Prints statistics including total file size and status codes.
    """
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))


def parse_line(line):
    """
    Parses a log line and extracts status code and file size.
    """
    parts = line.split()
    if len(parts) >= 9:
        status_code = parts[-2]
        file_size = parts[-1]

        return (
            int(status_code) if status_code.isdigit() else None,
            int(file_size) if file_size.isdigit() else 0
        )
    return None, 0


def main():
    """
    Main function to read input, parse lines, and print statistics.
    """
    total_size = 0
    status_codes = {}

    try:
        for i, line in enumerate(sys.stdin, 1):
            status_code, file_size = parse_line(line)
            if status_code is not None:
                total_size += file_size
                status_codes[status_code] = (
                    status_codes.get(status_code, 0) + 1
                )

            if i % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        # Handle keyboard interrupt, print final stats, and exit
        print_stats(total_size, status_codes)
        sys.exit(0)
    except BrokenPipeError:
        # Ignore BrokenPipeError when output not consumed by next process
        sys.exit(0)


if __name__ == "__main__":
    main()
