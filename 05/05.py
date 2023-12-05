#!/usr/bin/env python

import dataclasses

import util

@dataclasses.dataclass
class MappingRange:
    dst_range_start: int
    src_range_start: int
    range_leng: int

    def map(self, n: int):
        if n < self.src_range_start:
            return n
        if n > self.src_range_start + self.range_leng:
            return n

        offset = n - self.src_range_start

        return self.dst_range_start + offset


@dataclasses.dataclass
class Map:
    name: str
    ranges: list[MappingRange]

    @property
    def from_name(self) -> str:
        return self.name.split('-')[0]

    @property
    def to_name(self) -> str:
        return self.name.split(' ')[0].split('-')[-1]

    def map(self, n: int):
        for r in self.ranges:
            remapped = r.map(n)
            if remapped != n:
                return remapped
        return n


def iter_maps(lines: list[str]):
    for line in lines:
        if line.endswith(':'):
            # new entry
            current = Map(
                name=line.split(' ')[0],
                ranges=[],
            )
            continue
        if not line:
            # end of entry
            yield current
            continue

        d, s, l = line.split()
        current.ranges.append(
            MappingRange(
                dst_range_start=int(d),
                src_range_start=int(s),
                range_leng=int(l),
            )
        )
        continue

    # do mit forget about last element
    yield current


def iter_seeds(seeds: list[int]):
    while len(seeds) > 0:
        f = seeds[0]
        s = seeds[1]
        seeds = seeds[2:]

        yield from range(f, s)


def main():
    with open(util.input_file) as f:
        lines = [l.strip() for l in f.readlines()]

    seeds = [
        int(s) for s in lines[0].split(':')[-1].strip().split(' ')
    ]

    lines = lines[2:]

    mapping_ranges = tuple(iter_maps(lines=lines))

    for mr in mapping_ranges:
        seeds = map(mr.map, seeds)

    seeds = tuple(seeds)

    print(min(seeds))

if __name__ == '__main__':
    main()
