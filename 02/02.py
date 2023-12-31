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

    max_allowed = {
        'red': 12,
        'green': 13,
        'blue': 14,
    }

    possible_games = [g for g in games if g.possible(max_allowed)]

    sum_of_possible_game_ids = sum(g.id for g in possible_games)
    print(f'{sum_of_possible_game_ids=}')


if __name__ == '__main__':
    main()
