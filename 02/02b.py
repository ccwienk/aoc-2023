#!/usr/bin/env python

import dataclasses

import util

@dataclasses.dataclass
class Game:
    name: str
    subsets: list[dict[str, int]]

    @property
    def id(self):
        return int(self.name.split(' ')[-1])

    def possible(self, max_allowed: dict[str, int]):
        for subset in self.subsets:
            for colour, count in subset.items():
                allowed = max_allowed[colour]
                if count > allowed:
                    return False
        return True

    @property
    def minimum(self) -> dict[str, int]:
        minimum = {}
        for colour in 'red', 'blue', 'green':
            minimum[colour] = max(s.get(colour, 0) for s in self.subsets)

        return minimum


def parse_game(line: str) -> Game:
    line = line.strip()

    game, subsets = line.split(':')

    subsets = (s.strip() for s in subsets.split(';'))

    parsed_subsets = []

    for subset in subsets:
        parsed_subset = {}
        for count_colour_pair in subset.split(','):
            count, colour = count_colour_pair.strip().split(' ')
            count = int(count)

            parsed_subset[colour] = count

        parsed_subsets.append(parsed_subset)

    return Game(
        name=game,
        subsets=parsed_subsets,
    )


def main():
    with open(util.input_file) as f:
        lines = f.readlines()

    games = [parse_game(line) for line in lines]

    minimum_sets = (g.minimum for g in games)

    total = 0
    for s in minimum_sets:
        p = 1
        for c, v in s.items():
            if v == 0:
                continue
            p *= v
        total += p

    print(f'{total=}')


if __name__ == '__main__':
    main()
