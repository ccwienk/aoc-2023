#!/usr/bin/env python

import util


def main():
    with open(util.input_file) as f:
        directions = f.readline().strip()
        f.readline()
        node_lines = f.readlines()

    def iter_directions():
        # wrap directions forever
        while True:
            for c in directions:
                yield c


    nodes = {}

    for line in node_lines:
        node_id, remainder = line.strip().split(' = ')
        remainder = remainder.strip('(').strip(')')
        left, right = remainder.split(', ')

        nodes[node_id] = (left, right)

    node_id = 'AAA'
    for step, direction in enumerate(iter_directions(), 0):
        left, right = nodes[node_id]
        if node_id == 'ZZZ':
            print('done')
            break
        if direction == 'L':
            node_id = left
            left, right = nodes[left]
        else:
            node_id = right
            left, right = nodes[right]

    print(step)


if __name__ == '__main__':
    main()
