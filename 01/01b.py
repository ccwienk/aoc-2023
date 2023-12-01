#!/usr/bin/env python

import util


def find_digit(line: str, pos: str):
    nums = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9',
    }
    for c in line:
        if c.isdigit():
            if pos == 'first':
                return c
            val = c
        for name, value in nums.items():
            if line.startswith(name):
                if pos == 'first':
                    return value
                val = value

        line = line[1:]

    return val


def iter_calibration_values(lines):
    for line in lines:
        first_digit = find_digit(line, 'first')
        last_digit = find_digit(line, 'last')

        yield int(first_digit + last_digit)


def main():
    with open(util.input_file) as f:
        lines = f.readlines()

    calibration_values = tuple(iter_calibration_values(lines))

    sum_of_values = sum(calibration_values)

    print(f'{sum_of_values=}')


if __name__ == '__main__':
    main()
