#!/usr/bin/env python

import util


def is_asterisk(c: str):
    return c == '*'
    if c.isnumeric():
        return False
    if c == '.':
        return False
    return True


def has_asterisk_neighbour(rows, row, col):
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
        if is_asterisk(rows[row-1][col-1]):
            return True

    if check_above:
        if is_asterisk(rows[row-1][col]):
            return True

    if check_above and check_right:
        if is_asterisk(rows[row-1][col+1]):
            return True

    if check_left:
        if is_asterisk(rows[row][col-1]):
            return True

    if check_right:
        if is_asterisk(rows[row][col+1]):
            return True

    if check_below and check_left:
        if is_asterisk(rows[row+1][col-1]):
            return True

    if check_below:
        if is_asterisk(rows[row+1][col]):
            return True

    if check_below and check_right:
        if is_asterisk(rows[row+1][col+1]):
            return True

    return False


def iter_adjacent_numbers(
    row,
    col,
    rows,
    number_coordinates: list[list[tuple[int, int]]],
    numbers,
):
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

    for idx, number_coords in enumerate(number_coordinates):
        number_coords: list[tuple[int,int]] # [(row, col)]
        for nrow, ncol in number_coords:
            if check_above and check_left:
                if (row-1, col-1) == (nrow, ncol):
                    yield numbers[idx]
                    break

            if check_above:
                if (row-1, col) == (nrow, ncol):
                    yield numbers[idx]
                    break

            if check_above and check_right:
                if (row-1,col+1) == (nrow, ncol):
                    yield numbers[idx]
                    break

            if check_left:
                if (row,col-1) == (nrow, ncol):
                    yield numbers[idx]
                    break

            if check_right:
                if (row,col+1) == (nrow, ncol):
                    yield numbers[idx]
                    break

            if check_below and check_left:
                if (row+1,col-1) == (nrow, ncol):
                    yield numbers[idx]
                    break

            if check_below:
                if (row+1,col) == (nrow, ncol):
                    yield numbers[idx]
                    break

            if check_below and check_right:
                if (row+1,col+1) == (nrow, ncol):
                    yield numbers[idx]
                    break


def main():
    with open(util.input_file) as f:
        rows = [r.strip() for r in tuple(f.readlines())]

    rows_count = len(rows)
    cols_count = len(rows[0])

    numbers = []
    number_coordinates = [] # [[(row, column)]]; list of list of consecutive digits
    gear_candidate_coordinates = [] # [(row, column)]

    for ri, row in enumerate(rows):
        ci = 0

        while ci + 0 < cols_count:
            c = row[ci]

            if c == '.':
                ci += 1
                continue

            if c == '*':
                gear_candidate_coordinates.append((ri, ci))
                ci += 1
                continue

            num_coords = [] # coordinates of one consecutive sequence of digits (one number)
            is_adjacent = False
            while c.isnumeric():
                num_coords.append((ri, ci))
                if not is_adjacent:
                    is_adjacent |= has_asterisk_neighbour(rows, ri, ci)
                if not ci + 1 < cols_count:
                    break
                ci += 1
                c = row[ci]
                if c == '*':
                    gear_candidate_coordinates.append((ri, ci))

            if is_adjacent:
                num_str = ''
                for r, c in num_coords:
                    num_str += rows[r][c]
                numbers.append(int(num_str))
                number_coordinates.append(num_coords)

            ci += 1

    gear_ratio_sum = 0

    for row, column in gear_candidate_coordinates:
        adjacent_numbers = tuple(iter_adjacent_numbers(
            row,
            column,
            rows,
            number_coordinates,
            numbers,
        ))

        if len(adjacent_numbers) == 2:
            gear_ratio = adjacent_numbers[0] * adjacent_numbers[1]
            gear_ratio_sum += gear_ratio
        else:
            print(len(adjacent_numbers))

    print(f'{len(numbers)=}')
    print(f'{len(number_coordinates)}')
    print(f'{gear_ratio_sum=}')


if __name__ == '__main__':
    main()
