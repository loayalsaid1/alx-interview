#!/usr/bin/python3
"""
    I'M NOT QUITE SURE IF FOR SUCH A PROGRAM, I SHOULD MAKE FUNCTIONS AND
    SEPARATE SMALL TASKS AND THIS.. OR FOR SUCH SMALL ONES.
    a ONE FLOW WILL BE BETTER?
"""
import signal
import sys
import re

POSSIBLE_CODES = [200, 301, 400, 401, 403, 404, 405, 500]

total_size = 0
status_logs = {}


def print_logs():
    global total_size
    global status_logs
    global POSSIBLE_CODES

    print(f"File size: {total_size}")

    for code in POSSIBLE_CODES:
        if status_logs.get(code):
            print(f"{code}: {status_logs[code]}")


def handler(signum, frame):
    print_logs()


signal.signal(signal.SIGINT, handler)

if __name__ == "__main__":
    # For counting 10 lines then printing current logs
    try:
        temp_count = 0
        for line in sys.stdin:
            match = re.search(
                r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3} - "
                r"\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d+\]"
                r" \"GET /projects/260 HTTP/1.1\" (\d{3}) (\d+)$",
                line,
            )

            if match:
                status_code = int(match.group(1))
                status_logs[status_code] = status_logs.get(status_code, 0) + 1

                total_size += int(match.group(2))

                temp_count += 1

                if temp_count == 10:
                    print_logs()
                    temp_count = 0
    finally:
        print_logs()
