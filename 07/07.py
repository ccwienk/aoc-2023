#!/usr/bin/env python

import collections
import dataclasses
import enum

@dataclasses.dataclass
class Game:
    cards: list[int]
    bet: int
    idx: int
    line: str


import util

cards_map = {
    'A': 'D',
    'K': 'C',
    'Q': 'B',
    'J': 'A',
    'T': '9',
    '9': '8',
    '8': '7',
    '7': '6',
    '6': '5',
    '5': '4',
    '4': '3',
    '3': '2',
    '2': '1',
}


class Type(enum.IntEnum):
    FIVE = 7 # five of a kind
    FOUR = 6 # four of a kind
    FULL_HOUSE = 5
    THREE = 4 # three of a kind
    TWO_PAIRS = 3
    ONE_PAIR = 2
    HIGH_CARD = 1


def determine_type(game: Game):
    groups = collections.defaultdict(list)
    for c in sorted(game.cards):
        groups[c].append(c)

    if len(groups) == 1:
        t = Type.FIVE
        return t

    elif len(groups) == 2:
        lesser, greater = groups.values()
        # two cases: full-house (2 + 3), four (1, 4)
        if len(lesser) in (2, 3): # full-house
            t = Type.FULL_HOUSE
            return t

        # four-of-a-kind
        t = Type.FOUR
        return t

    elif len(groups) == 3:
        first, second, third = groups.values()

        # two pairs (AA, BB, x)
        if len(first) == 2:
            t = Type.TWO_PAIRS
            if len(second) == 2:
                score = (first[0], second[0])
            else:
                score = (first[0], third[0])
            return t
        if len(second) == 2:
            t = Type.TWO_PAIRS
            # first group already checked to not have two members
            return t

        # three of a kind (AAA, B, x)
        t = Type.THREE
        if len(first) == 3:
            return t
        if len(second) == 3:
            return t
        return t

    elif len(groups) == 4:
        return Type.ONE_PAIR

    return Type.HIGH_CARD


def to_score(game: Game):
    t = determine_type(game)

    return int(str(t.value) + ''.join(n for n in game.cards), base=16)


def parse_game(line: str, idx: int):
    cards, bet = line.strip().split()
    cards = [cards_map[c] for c in cards]
    bet = int(bet)

    return Game(
        cards=cards,
        bet=bet,
        line=line,
        idx=idx,
    )


def main():
    with open(util.input_file) as f:
        lines = [l.strip() for l in f.readlines()]

    games = [parse_game(l, idx) for idx, l in enumerate(lines)]

    games = sorted(games, key=to_score)

    total_score = 0
    for rank, game in enumerate(games, 1):
        total_score += rank * game.bet

    print(f'{total_score=}')


if __name__ == '__main__':
    main()
