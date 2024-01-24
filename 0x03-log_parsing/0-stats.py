#!/usr/bin/python3
import sys


def print_stats(total_size, status_codes):
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))


def parse_line(line):
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
        print_stats(total_size, status_codes)
        sys.exit(0)
    except BrokenPipeError:
        # Ignore BrokenPipeError when output is not consumed by next process
        sys.exit(0)


if __name__ == "__main__":
    main()
