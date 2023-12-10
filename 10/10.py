#!/usr/bin/env python

import dataclasses

import util

# | is a vertical pipe connecting north and south.
# - is a horizontal pipe connecting east and west.
# L is a 90-degree bend connecting north and east.
# J is a 90-degree bend connecting north and west.
# 7 is a 90-degree bend connecting south and west.
# F is a 90-degree bend connecting south and east.
# . is ground; there is no pipe in this tile.
# S is the starting position of the animal; there is a pipe on this tile, but
#   your sketch doesn't show what shape the pipe has.


@dataclasses.dataclass
class Directions:
    top: bool
    left: bool
    right: bool
    down : bool


def directions_for_char(curr: str):
    if curr in ('|', 'L', 'J', 'S'):
        top = True
    else:
        top = False

    if curr in ('|', '7', 'F', 'S'):
        down = True
    else:
        down = False

    if curr in ('-', 'J', '7', 'S'):
        left = True
    else:
        left = False

    if curr in ('-', 'L', 'F', 'S'):
        right = True
    else:
        right = False

    return Directions(
        top=top,
        left=left,
        right=right,
        down=down,
    )


def directions(
    rows,
    r,
    c,
    rows_count,
    cols_count,
):
    curr = rows[r][c]

    d = directions_for_char(curr)

    if r == 0:
        d.top = False

    if not r < rows_count:
        d.down = False

    if c == 0:
        d.left = False

    if not c < cols_count:
        d.right = False

    return d


def iter_available(rows: list[str], r, c, rows_count: int, cols_count: int):
    d = directions(rows, r, c, rows_count, cols_count)

    if d.top:
        nf = (r-1, c)
        n = rows[nf[0]][nf[1]]
        nd = directions_for_char(n)
        if nd.down:
            yield nf
    if d.left:
        nf = (r, c-1)
        n = rows[nf[0]][nf[1]]
        nd = directions_for_char(n)
        if nd.right:
            yield nf
    if d.right:
        nf = (r, c+1)
        n = rows[nf[0]][nf[1]]
        nd = directions_for_char(n)
        if nd.left:
            yield nf
    if d.down:
        nf = (r+1, c)
        n = rows[nf[0]][nf[1]]
        nd = directions_for_char(n)
        if nd.top:
            yield nf


def main():
    with open(util.input_file) as f:
        rows = [l.strip() for l in f.readlines()]

    rows_count = len(rows)
    cols_count = len(rows[0])

    for ri, row in enumerate(rows):
        if 'S' in row:
            start = (ri, row.index('S'))

    print(f'{start=}')
    print()

    whence = start
    curr_pos = start

    steps = 0
    while True:
        print(f'{curr_pos=}')
        print(f'{whence=}')
        available = set(
            iter_available(rows, *curr_pos, rows_count, cols_count)
        )
        if whence in available:
            available.remove(whence)

        # there should actually only be one left, except for right at the start
        whence = curr_pos
        curr_pos = available.pop()
        print(f'to: {curr_pos=}')
        print()

        steps += 1

        if curr_pos == start:
            break

    print(steps)
    print(f'longest dist: {int(steps/2)}')


if __name__ == '__main__':
    main()
