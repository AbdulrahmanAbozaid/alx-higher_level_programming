#!/usr/bin/python3
'''Pyc User'''


from sys import stdin


status_codes = {
        '200': 0,
        '301': 0,
        '400': 0,
        '401': 0,
        '403': 0,
        '404': 0,
        '405': 0,
        '500': 0
        }

total_size = i = 0


def printer():
    '''Printer Func'''
    print(f"File size: {total_size}")
    for key, val in sorted(status_codes.items()):
        if val > 0:
            print('{:s}: {:d}'.format(key, val))


try:
    for line in stdin:
        splitted = line.split()
        if len(splitted) >= 2:
            status = splitted[-2]
            total_size += int(splitted[-1])
            if status in status_codes:
                status_codes[status] += 1
        i += 1

        if i % 10 == 0:
            printer()
        printer()
except KeyboardInterrupt as e:
    printer()
