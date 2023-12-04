#!/usr/bin/env python

import collections
import dataclasses
import util


@dataclasses.dataclass
class Card:
    name: str
    winning_numbers: set[int]
    numbers: set[int]

    @property
    def number(self) -> int:
        return int(self.name.split()[-1])

    @property
    def score(self):
        matches = len(self.winning_numbers & self.numbers)

        if not matches:
            return 0

        return pow(2, matches - 1)

    @property
    def matching(self):
        return len(self.winning_numbers & self.numbers)



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

    cards = [
        parse_card(l) for l in lines
    ]

    card_counts = collections.defaultdict(lambda: 1)

    for idx, card in enumerate(cards):
        if (matching := card.matching) == 0:
            continue

        num_cards = card_counts[idx]

        for win_idx_offset in range(matching):
            card_counts[win_idx_offset + 1 + idx] += num_cards

    cards_count = 0

    for idx, _ in enumerate(cards):
        cards_count += card_counts[idx]

    print(f'{cards_count=}')


if __name__ == '__main__':
    main()
