#!/usr/bin/env python

import util


def calc_next_diffs(seq: list[int]):
    i = 0
    diffs = []
    while i + 1 < len(seq):
        diffs.append(seq[i+1] - seq[i])
        i += 1

    return diffs


def calc_diffs(seq: list[int]) -> list[list[int]]:
    seqs: list[list[int]] = [seq]
    i = 0
    while True:
        diffs = calc_next_diffs(seqs[i])
        seqs.append(diffs)
        i += 1
        for d in diffs:
            if d != 0:
                break
        else:
            # last diff was all zeroes
            return seqs


def extrapolate(seqs: list[list[int]]):
    i = len(seqs) - 1
    while i > 0:
        top = seqs[i]
        nex = seqs[i-1]

        nex.insert(0, nex[0] - top[0])

        i -= 1

    return seqs[0][0]



def main():
    sequences = []
    with open(util.input_file) as f:
        while (line := f.readline()):
            sequences.append([int(n) for n in line.strip().split()])

    total = 0
    for seq in sequences:
        total += extrapolate(calc_diffs(seq))

    print(f'{total=}')

if __name__ == '__main__':
    main()
