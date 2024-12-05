import re
from itertools import product

xmas_pattern = re.compile(r'(?=(XMAS|SAMX))')
mas_pattern = re.compile(r'MAS|SAM')

def get_diagonal_lines(grid, Lx):
    """Generate diagonal lines (top-left to bottom-right and reverse)."""
    pad = "." * (Lx - 1)
    padded_grid = [pad + row + pad for row in grid]
    
    def diagonal_lines(padded_grid):
        shifts = [row[shift:] for shift, row in enumerate(padded_grid)]
        return " ".join("".join(chars) for chars in zip(*shifts))

    return diagonal_lines(padded_grid), diagonal_lines(padded_grid[::-1])

def count_xmas_patterns(grid):
    """Count XMAS/SAMX patterns in all directions."""
    horizontal = " ".join(grid)
    vertical = " ".join("".join(row) for row in zip(*grid))
    
    diagonal, antidiagonal = get_diagonal_lines(grid, len(grid[0]))
    full_schema = " ".join((horizontal, vertical, diagonal, antidiagonal))
    
    return len(xmas_pattern.findall(full_schema))

def count_mas_patterns(grid):
    """Count valid MAS/SAM patterns based on diagonal rules."""
    Lx, Ly = len(grid[0]), len(grid)
    count = 0
    
    for y, x in product(range(1, Ly - 1), range(1, Lx - 1)):
        if grid[y][x] == "A":
            diagonal = grid[y-1][x-1] + grid[y][x] + grid[y+1][x+1]
            antidiagonal = grid[y-1][x+1] + grid[y][x] + grid[y+1][x-1]
            if mas_pattern.match(diagonal) and mas_pattern.match(antidiagonal):
                count += 1
                
    return count

if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().splitlines()

    # Part 1
    xmas_count = count_xmas_patterns(lines)
    print(xmas_count)

    # Part 2
    mas_count = count_mas_patterns(lines)
    print(mas_count)