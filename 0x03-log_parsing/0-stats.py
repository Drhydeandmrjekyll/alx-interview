#!/usr/bin/python3
"""This module read stdin and compute metrics"""
import sys


def print_stats(total_size, status_counts):
    """Print accumulated metrics.

    Args:
        size (int): The accumulated read file size.
        status_codes (dict): The accumulated count of status codes.
    """
    print("File size: {}".format(total_size))
    for key in sorted(status_counts):
        print("{}: {}".format(key, status_counts[key]))


total_size = 0
status_counts = {}
valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
count = 0
try:
    for line in sys.stdin:
        if count == 10:
            print_stats(total_size, status_counts)
            count = 1
        else:
            count += 1
        line = line.split()
        try:
            total_size += int(line[-1])
        except (IndexError, ValueError):
            pass
        try:
            if line[-2] in valid_codes:
                if status_counts.get(line[-2], -1) == -1:
                    status_counts[line[-2]] = 1
                else:
                    status_counts[line[-2]] += 1
        except IndexError:
            pass
    print_stats(total_size, status_counts)
except KeyboardInterrupt:
    print_stats(total_size, status_counts)
    raise
