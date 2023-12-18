#!/usr/bin/env python

import functools

import util


def _getp(row: int, col: int, rows: list[list[str]]):
    return rows[row][col]


def _setp(row: int, col: int, v: str, rows: list[list[str]]):
    rows[row][col] = v


empty = '.'
immut = '#'
boldr = 'O'

up = 'up'



def main():
    with open(util.input_file) as f:
        rows = [[c for c in row.strip()] for row in f.readlines()]

    getp = functools.partial(_getp, rows=rows)
    setp = functools.partial(_setp, rows=rows)

    def mv(src: tuple[int, int], direction: str):
        src_row, src_col = src
        v = getp(src_row, src_col)
        setp(src_row, src_col, empty)

        if direction == up:
            tgt_row = src_row - 1
            tgt_col = src_col
        else:
            raise ValueError(direction)

        setp(tgt_row, tgt_col, v)

    def getnp(row: int, col: int, direction: str):
        if direction == up:
            tgt_row = row - 1
            tgt_col = col
        else:
            raise ValueError(direction)

        return getp(tgt_row, tgt_col)


    for _ in range(0, 100):
        for row in range(1, 100): # skip north (=top)most row
            for col in range(0, 100):
                cur = getp(row, col)
                if cur in (empty, immut):
                    continue # only boulders can be moved

                above = getnp(row, col, up)

                if not above == empty:
                    continue

                # current point is boulder + entry above is free: -> mv boulder one up
                mv((row, col), up)

    total_weight = 0

    for idx, row in enumerate(rows):
        weight = 100 - idx
        for c in row:
            if c == boldr:
                total_weight += weight

    print(f'{total_weight=}')


if __name__ == '__main__':
    main()
