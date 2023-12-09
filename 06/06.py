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

        time_line = time_line.strip()
        dist_line = dist_line.strip()

    times = [int(n) for n in time_line.split()[1:]]
    dists = [int(d) for d in dist_line.split()[1:]]

    print(f'{times=} {dists=}')

    better_count_total_product = 1

    for time, dist in zip(times, dists):
        better_count = 0
        for s in range(dist):
            reached_dist = calc_dist(s, time)
            if reached_dist > dist:
                better_count += 1
        better_count_total_product *= better_count


    print(f'{better_count_total_product=}')

if __name__ == '__main__':
    main()
