#!/usr/bin/env python

import util


def iter_calibration_values(lines):
    for line in lines:
        digits = [c for c in line if c.isdigit()]

        yield int(digits[0] + digits[-1])


def main():
    with open(util.input_file) as f:
        lines = f.readlines()

    calibration_values = tuple(iter_calibration_values(lines))

    sum_of_values = sum(calibration_values)

    print(f'{sum_of_values=}')


if __name__ == '__main__':
    main()
