import re

with open("input.txt", "r") as file:
    lines = file.readlines()

part1_total = sum(
    int(a) * int(b)
    for line in lines
    for a, b in re.findall(r"mul\((\d+),(\d+)\)", line)
)
print(f"Part 1: {part1_total}")

part2_total = 0
state = True  # Tracks whether "on" or "off" mode is active

for line in lines:
    actions = sorted(
        re.finditer(r"(do\(\)|don't\(\)|mul\((\d+),(\d+)\))", line),
        key=lambda match: match.start()
    )

    for match in actions:
        action = match.group(0)
        if action == "do()":
            state = True
        elif action == "don't()":
            state = False
        elif state:  # Only process mul(x, y) when state is True
            a, b = map(int, match.groups()[1:])
            part2_total += a * b

print(f"Part 2: {part2_total}")