#!/usr/bin/env python

import itertools

import util


def manhattan_distance(p1: tuple[int, int], p2: tuple[int, int]):
    x1, y1 = p1
    x2, y2 = p2

    return abs(x1 - x2) + abs(y1 - y2)


def iter_stars(rows: list[str]):
    for ri, row in enumerate(rows):
        for ci, c in enumerate(row):
            if c == '#':
                # todo: handle blank-line|column-duplication
                yield (ri, ci)


def effective_coords(row: int, col: int, blank_rows, blank_cols):
    row_offset = 0
    col_offset = 0

    for blank_row in blank_rows:
        if row > blank_row:
            # row is past blank line (-> blank line counts double)
            row_offset += (1000000 -1)
        else:
            break

    for blank_col in blank_cols:
        if col > blank_col:
            # col is past blank line (-> blank col counts double)
            col_offset += (1000000 -1)
        else:
            break

    return (row + row_offset, col + col_offset)


def main():
    with open(util.input_file) as f:
        rows = [r.strip() for r in f.readlines()]

    blank_rows = []
    for ri, row in enumerate(rows):
        for c in row:
            if c == '#':
                break
        else:
            blank_rows.append(ri)

    blank_cols = []
    for ci in range(len(rows[0])):
        for ri, row in enumerate(rows):
            if rows[ri][ci] == '#':
                break
        else:
            blank_cols.append(ci)

    star_coords = iter_stars(rows)

    star_coords = [effective_coords(r,c, blank_rows, blank_cols) for r,c in star_coords]

    total_dist = 0

    for a,b in itertools.combinations(star_coords, 2):
        total_dist += manhattan_distance(a, b)

    print(f'{total_dist=}')


if __name__ == '__main__':
    main()
