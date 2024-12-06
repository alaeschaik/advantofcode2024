from typing import Set, Tuple

rotation = "^>v<"

def parse_input(file_path: str) -> Tuple[Set[Tuple[int, int]], str, Tuple[int, int], int, int]:
    """Parse the input file and extract obstacles, initial guard direction, position, and grid size."""
    obstacles = set()
    guard_direction, guard_position = "", (0, 0)
    max_x, max_y = 0, 0

    with open(file_path) as f:
        for y, line in enumerate(f):
            line = line.strip()
            max_y = y + 1
            max_x = len(line)
            for x, char in enumerate(line):
                if char == "#":
                    obstacles.add((x, y))
                elif char in rotation:
                    guard_direction, guard_position = char, (x, y)

    return obstacles, guard_direction, guard_position, max_x, max_y


def calculate_guard_path(
    guard: Tuple[str, Tuple[int, int]], obstacles: Set[Tuple[int, int]], max_x: int, max_y: int
) -> Set[Tuple[int, int]]:
    """Calculate the path of the guard until it enters a loop or exits the grid."""
    directions = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}

    seen_states = set()
    while guard not in seen_states:
        seen_states.add(guard)
        direction, position = guard
        dx, dy = directions[direction]
        new_position = (position[0] + dx, position[1] + dy)

        # Rotate if the next position is blocked
        while new_position in obstacles:
            direction = rotation[(rotation.index(direction) + 1) % len(rotation)]
            dx, dy = directions[direction]
            new_position = (position[0] + dx, position[1] + dy)

        # Exit if guard moves out of bounds
        if not (0 <= new_position[0] < max_x and 0 <= new_position[1] < max_y):#
            break

        guard = (direction, new_position)

    return {state[1] for state in seen_states}


def is_guard_in_loop(
    guard: Tuple[str, Tuple[int, int]], obstacles: Set[Tuple[int, int]], max_x: int, max_y: int
) -> bool:
    """Check if a guard eventually loops given its starting state and grid configuration."""
    seen_states = set()
    directions = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}

    while guard not in seen_states:
        seen_states.add(guard)
        direction, position = guard
        dx, dy = directions[direction]
        new_position = (position[0] + dx, position[1] + dy)

        # Rotate if the next position is blocked
        while new_position in obstacles:
            direction = rotation[(rotation.index(direction) + 1) % len(rotation)]
            dx, dy = directions[direction]
            new_position = (position[0] + dx, position[1] + dy)

        # Exit if guard moves out of bounds
        if not (0 <= new_position[0] < max_x and 0 <= new_position[1] < max_y):
            return False

        guard = (direction, new_position)

    return True


def part1(file_path: str) -> Set[Tuple[int, int]]:
    """Solve the first part of the puzzle."""
    obstacles, guard_direction, guard_position, max_x, max_y = parse_input(file_path)
    path = calculate_guard_path((guard_direction, guard_position), obstacles, max_x, max_y)
    print(f"Part 1: {len(path)} unique positions visited.")
    return path


def part2(file_path: str, path: Set[Tuple[int, int]]) -> None:
    """Solve the second part of the puzzle."""
    obstacles, guard_direction, guard_position, max_x, max_y = parse_input(file_path)
    result = sum(
        is_guard_in_loop((guard_direction, guard_position), obstacles | {pos}, max_x, max_y)
        for pos in path
    )
    print(f"Part 2: {result} positions cause the guard to loop.")


if __name__ == "__main__":
    input_file = "input.txt"
    path_part1 = part1(input_file)
    part2(input_file, path_part1)
