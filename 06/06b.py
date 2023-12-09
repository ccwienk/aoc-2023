#!/usr/bin/env python

import util


def calc_dist(speed: int, allowedtime: int):
    # speed costs speed amount of time for speeding up
    # speed must be less or equal to allowedtime
    allowedtime -= speed

    dist = speed * allowedtime

    return dist


def main():
    with open(util.input_file) as f:
        time_line,  dist_line = f.readlines()

        time_line: str = time_line.strip().split(':')[-1]
        dist_line: str = dist_line.strip().split(':')[-1]

    time = int(time_line.replace(' ', ''))
    dist = int(dist_line.replace(' ', ''))

    print(f'{time=} {dist=}')

    for s in range(int(time / 9), time):
        d = calc_dist(s, time)
        if d > dist:
            print(f'lowest   "fast-enough" speed: {s=}')
            lowest = s
            break

    for s in range(int(time - time / 9), 0, -1):
        d = calc_dist(s, time)
        if d > dist:
            print(f'greatest "fast-enough" speed: {s=}')
            greatest = s
            break

    print(f'{(greatest - lowest) + 1=}')

    exit(0)

    better_count = 0
    for s in range(dist):
        reached_dist = calc_dist(s, time)
        print(reached_dist)

        if s > 200:
            return
        if reached_dist > dist:
            better_count += 1
    better_count_total_product *= better_count


    print(f'{better_count_total_product=}')

if __name__ == '__main__':
    main()
