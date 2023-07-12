#!/usr/bin/python3
"""Log parsing module"""
import sys
import collections


def main():
    """Reads stdin line by line and computes metrics."""
    total_size = 0
    status_counts = collections.defaultdict(int)

    sys.stdin.buffer_size = 1024 * 1024

    for line in sys.stdin:
        line = line.rstrip()
        parts = line.split(" ")
        if len(parts) >= 4:
            if parts[4].isdigit():
                status_code = int(parts[4])
                file_size = int(parts[5])
                total_size += file_size
                status_counts[status_code] += 1
            if len(status_counts) % 10 == 0 or line == "":
                print("File size: {}".format(total_size))
                for status_code, count in status_counts.items():
                    print("{}: {}".format(status_code, count))
                sys.stdout.flush()


if __name__ == "__main__":
    main()
