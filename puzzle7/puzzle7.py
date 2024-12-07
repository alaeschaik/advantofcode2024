import fileinput
import re
import itertools


def get_calibration(pattern: str) -> int:
    total = 0
    for line in fileinput.input('input.txt'):
        result, *parts = map(int, re.findall(r"-?\d+", line))
        for operators in itertools.product(pattern, repeat=len(parts) - 1):
            expression = parts[0]
            for operator, value in zip(operators, parts[1:]):
                if operator == '*':
                    expression *= value
                elif operator == '+':
                    expression += value
                elif operator == '|':
                    expression = int(f"{expression}{value}")
            if expression == result:
                total += result
                break
    return total


pattern_part1 = "+*"
pattern_part2 = "+*|"

print(f"Part 1: {get_calibration(pattern_part1)}")
print(f"Part 2: {get_calibration(pattern_part2)}")
