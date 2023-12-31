#!/usr/bin/env python

import dataclasses
import util


@dataclasses.dataclass
class Card:
    name: str
    winning_numbers: set[int]
    numbers: set[int]

    @property
    def score(self):
        matches = len(self.winning_numbers & self.numbers)

        if not matches:
            return 0

        return pow(2, matches - 1)



def parse_card(line: str):
    name, numbers = line.split(':')
    winning, have = numbers.split('|')

    return Card(
        name=name,
        winning_numbers={int(n) for n in winning.split()},
        numbers={int(n) for n in have.split()},
    )


def main():
    with open(util.input_file) as f:
        lines = (l.strip() for l in f.readlines())

    cards = (
        parse_card(l) for l in lines
    )

    score_sum = sum((c.score for c in cards))

    print(f'{score_sum=}')


if __name__ == '__main__':
    main()
