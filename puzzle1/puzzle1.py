from collections import Counter

with open("input.txt", "r") as file:
    data = file.read().strip().split("\n")

left, right = zip(*(map(int, line.split("   ")) for line in data))

sorted_left = sorted(left)
sorted_right = sorted(right)
part1_result = sum(abs(nl - nr) for nl, nr in zip(sorted_left, sorted_right))
print(f"Part 1: {part1_result}")

right_counts = Counter(right)
part2_result = sum(n * right_counts[n] for n in left)
print(f"Part 2: {part2_result}")
