#!/usr/bin/env python

import collections

import util


def crishash(s: str):
    v = 0

    for c in s:
        v += ord(c)
        v *= 17
        v %= 256

    return v


op_rm = object()
op_ins = object()


def main():
    def parse_op(op: str):
        if op.endswith('-'):
            label = op[:-1]
            return op_rm, crishash(label), label, None
        label, operand = op.split('=')

        return op_ins, crishash(label), label, int(operand)

    with open(util.input_file) as f:
        strs = f.read().strip().split(',')


    boxes = collections.defaultdict(list)

    for op, boxidx, label, new_lenswidth in (parse_op(s) for s in strs):
        box = boxes[boxidx]

        if op is op_rm:
            for box_label, lenswidth in box:
                if box_label == label:
                    box.remove((box_label, lenswidth))
            continue
        elif op is op_ins:
            for idx, (box_label, lenswidth) in enumerate(box):
                if box_label == label:
                    box.insert(idx + 1, (box_label, new_lenswidth))
                    box.pop(idx)
                    break
            else:
                box.append((label, new_lenswidth))
        else:
            raise ValueError(op)

    total = 0

    for idx, box in boxes.items():
        for box_idx, (_, lensleng) in enumerate(box, 1):
            value = (idx + 1) * box_idx * lensleng
            total += value

    print(f'{total=}')


if __name__ == '__main__':
    main()
