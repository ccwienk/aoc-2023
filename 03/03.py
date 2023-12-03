#!/usr/bin/env python

import util


def is_symbol(c: str):
    if c.isnumeric():
        return False
    if c == '.':
        return False
    return True


def has_symbol_neighbour(rows, row, col):
    rows_count = len(rows)
    cols_count = len(rows[0])

    if row > 0:
        check_above = True
    else:
        check_above = False

    if row + 1 < rows_count:
        check_below = True
    else:
        check_below =False

    if col > 0:
        check_left = True
    else:
        check_left = False

    if col + 1 < cols_count:
        check_right = True
    else:
        check_right = False

    if check_above and check_left:
        if is_symbol(rows[row-1][col-1]):
            return True

    if check_above:
        if is_symbol(rows[row-1][col]):
            return True

    if check_above and check_right:
        if is_symbol(rows[row-1][col+1]):
            return True

    if check_left:
        if is_symbol(rows[row][col-1]):
            return True

    if check_right:
        if is_symbol(rows[row][col+1]):
            return True

    if check_below and check_left:
        if is_symbol(rows[row+1][col-1]):
            return True

    if check_below:
        if is_symbol(rows[row+1][col]):
            return True

    if check_below and check_right:
        if is_symbol(rows[row+1][col+1]):
            return True

    return False


def main():
    with open(util.input_file) as f:
        rows = [r.strip() for r in tuple(f.readlines())]

    rows_count = len(rows)
    cols_count = len(rows[0])

    numbers = []

    for ri, row in enumerate(rows):
        ci = 0

        while ci + 0 < cols_count:
            c = row[ci]

            if c == '.':
                ci += 1
                continue

            num_coords = []
            is_adjacent = False
            while c.isnumeric():
                num_coords.append((ri, ci))
                if not is_adjacent:
                    is_adjacent |= has_symbol_neighbour(rows, ri, ci)
                ci += 1
                if not ci < cols_count:
                    break
                c = row[ci]

            if is_adjacent:
                num_str = ''
                for r, c in num_coords:
                    num_str += rows[r][c]
                numbers.append(int(num_str))

            ci += 1

    print(f'{sum(numbers)=}')


if __name__ == '__main__':
    main()
