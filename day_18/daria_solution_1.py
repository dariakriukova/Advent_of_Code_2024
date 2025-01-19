import numpy as np
from collections import deque

grid_size = 71 
grid = np.full((grid_size, grid_size), '.')

with open('day_18/test_input.txt', 'r') as f:
    falling_bytes = [tuple(map(int, line.strip().split(','))) for line in f][:1024]

for x, y in falling_bytes:
    grid[y, x] = '#'


def shortest_path(grid, start, end):
    rows, cols = grid.shape
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(start, 0)])
    visited = set()
    visited.add(start)

    while queue:
        (x, y), steps = queue.popleft()

        if (x, y) == end:
            return steps

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited and grid[nx, ny] == '.':
                visited.add((nx, ny))
                queue.append(((nx, ny), steps + 1))

    return -1

start = (0, 0)
end = (70, 70)

min_steps = shortest_path(grid, start, end)
print(f"Minimum number of steps needed to reach the exit: {min_steps}")
