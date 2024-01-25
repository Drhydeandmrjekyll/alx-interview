#!/usr/bin/python3
"""Log Parsing Script - Reads stdin, computes metrics,
and prints statistics."""

import sys


def print_metrics(total_size, status_counts):
    """Prints accumulated metrics including total
    file size and status code counts."""
    print("Total file size: {}".format(total_size))
    for code in sorted(status_counts):
        print("{}: {}".format(code, status_counts[code]))


total_size = 0
status_counts = {}
valid_status_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
line_count = 0

try:
    # Looping through each line in stdin
    for line in sys.stdin:
        # Printing accumulated metrics every 10 lines
        if line_count == 10:
            print_metrics(total_size, status_counts)
            line_count = 1
        else:
            line_count += 1
        # Parsing line and updating accumulated metrics
        line = line.split()
        try:
            total_size += int(line[-1])
        except (IndexError, ValueError):
            pass
        try:
            if line[-2] in valid_status_codes:
                if status_counts.get(line[-2], -1) == -1:
                    status_counts[line[-2]] = 1
                else:
                    status_counts[line[-2]] += 1
        except IndexError:
            pass

    # Printing final accumulated metrics
    print_metrics(total_size, status_counts)

except KeyboardInterrupt:
    # Handle keyboard interrupt by printing final accumulated metrics
    print_metrics(total_size, status_counts)
    raise  # Re-raising KeyboardInterrupt to exit gracefully with error message
