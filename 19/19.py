#!/usr/bin/env python

import dataclasses

import util

reject = 'R'
accept = 'A'
switch = object()
skip = object()


@dataclasses.dataclass
class RuleSet:
    name: str
    rules: list[str]


@dataclasses.dataclass
class Part:
    x: int = None
    m: int = None
    a: int = None
    s: int = None

    @property
    def total(self):
        return self.x + self.m + self.a + self.s


def parse_part(line: str) -> Part:
    line = line.strip('{}')
    part = Part()
    for part_str in line.split(','):
        p, v = part_str.split('=')
        setattr(part, p, int(v))

    return part


def eval_rule(rule: str, part: Part):
    if rule == reject:
        return reject, None
    elif rule == accept:
        return accept, None
    if not ':' in rule:
        # rule's value is id of another rule
        return switch, rule

    # if this line is reached, there is an expression to evaluate
    expr, result = rule.split(':')
    if eval(expr, dataclasses.asdict(part)):
        if result in (reject, accept):
            return result, None
        return switch, result
    else:
        # try next rule
        return skip, None


def parse_ruleset(line: str) -> RuleSet:
    name, remainder = line.split('{')
    remainder = remainder.strip('}')

    return RuleSet(
        name=name,
        rules=remainder.split(','),
    )


def main():
    parts = []
    rulesets = {}

    with open(util.input_file) as f:
        for line in  f.readlines():
            line = line.strip()
            if not line:
                continue

            if line.startswith('{'):
                parts.append(parse_part(line))
            else:
                ruleset = parse_ruleset(line)
                rulesets[ruleset.name] = ruleset

    accepted = []

    for part in parts:
        ruleset = rulesets['in']
        while True:
            for rule in ruleset.rules:
                operation, operand = eval_rule(rule, part)

                if operation == accept:
                    accepted.append(part)
                    break
                if operation == reject:
                    break
                if operation == skip:
                    continue # try next rule
                if operation == switch:
                    break
            else:
                raise ValueError('ran out of rules')

            # also break of outer loop if part was accepted/rejected
            if operation in (accept, reject):
                break

            if operation == switch:
                ruleset = rulesets[operand]
                continue

            # should not be possible to happen
            raise ValueError('ran out of rules')

    total_parts_score = 0

    for ap in accepted:
        total_parts_score += ap.total

    print(f'{total_parts_score=}')


if __name__ == '__main__':
    main()
