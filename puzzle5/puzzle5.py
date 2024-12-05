from collections import defaultdict, deque

def parse_input(file_path):
  with open(file_path, 'r') as file:
    lines = [line.strip() for line in file]  # Read and strip lines at once

  divider = lines.index("")
  rules = [tuple(map(int, line.split('|'))) for line in lines[:divider]]
  updates = [list(map(int, line.split(','))) for line in lines[divider + 1:]]

  return rules, updates

def is_valid_order(update, rules):
  """
  Check if the given update respects the ordering rules.
  """
  position = {page: i for i, page in enumerate(update)}
  return all(position[x] < position[y] for x, y in rules if x in position and y in position)

def topological_sort(update, rules):
  """
  Perform a topological sort to correctly order the update based on the rules.
  """
  graph = defaultdict(list)
  indegree = {page: 0 for page in set(update)}

  for x, y in rules:
    if x in update and y in update:
      graph[x].append(y)
      indegree[y] += 1

  queue = deque([page for page in update if indegree[page] == 0])
  sorted_update = []

  while queue:
    current = queue.popleft()
    sorted_update.append(current)
    for neighbor in graph[current]:
      indegree[neighbor] -= 1
      if indegree[neighbor] == 0:
        queue.append(neighbor)

  return sorted_update

def process_updates(file_path):
  """
  Process the updates and compute results for both parts of the puzzle.
  """
  rules, updates = parse_input(file_path)

  valid_updates = [update for update in updates if is_valid_order(update, rules)]
  invalid_updates = [update for update in updates if update not in valid_updates]

  part1_sum = sum(update[len(update) // 2] for update in valid_updates)

  corrected_updates = [topological_sort(update, rules) for update in invalid_updates]
  part2_sum = sum(update[len(update) // 2] for update in corrected_updates)

  return part1_sum, part2_sum

if __name__ == "__main__":
  part1_result, part2_result = process_updates("input.txt")

  print("Part 1:", part1_result)
  print("Part 2:", part2_result)