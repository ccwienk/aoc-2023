#!/usr/bin/env python

import util


def crishash(s: str):
    v = 0

    for c in s:
        v += ord(c)
        v *= 17
        v %= 256

    return v


def main():
    with open(util.input_file) as f:
        strs = f.read().strip().split(',')

    total = 0

    for s in strs:
        total += crishash(s)

    print(f'{total=}')


if __name__ == '__main__':
    main()
