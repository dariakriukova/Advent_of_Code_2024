from collections import deque

def solve_race_condition(grid):
    rows = len(grid)
    cols = len(grid[0])

    # Find S and E
    start = None
    end = None
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 'S':
                start = (r, c)
            elif grid[r][c] == 'E':
                end = (r, c)

    # Directions for normal BFS
    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    # BFS that respects walls
    def bfs(start_pos):
        dist = [[float('inf')]*cols for _ in range(rows)]
        queue = deque()
        dist[start_pos[0]][start_pos[1]] = 0
        queue.append(start_pos)
        while queue:
            r, c = queue.popleft()
            for dr, dc in directions:
                nr, nc = r+dr, c+dc
                if 0<=nr<rows and 0<=nc<cols:
                    if grid[nr][nc] != '#' and dist[nr][nc] == float('inf'):
                        dist[nr][nc] = dist[r][c] + 1
                        queue.append((nr, nc))
        return dist

    distanceS = bfs(start)
    distanceE = bfs(end)
    normalDist = distanceS[end[0]][end[1]]
    if normalDist == float('inf'):
        return 0  # No path at all

    # For each cell, gather reachable cells in up to 2 steps ignoring walls
    # We'll do a quick BFS limited to 2 steps ignoring walls
    def two_step_ignore_walls(r, c):
        result = []  # (rB, cB, cost)
        visited = set()
        queue = deque()
        queue.append((r, c, 0))
        visited.add((r, c))
        while queue:
            rr, cc, steps = queue.popleft()
            if steps > 0:  # store after at least 1 move
                result.append((rr, cc, steps))
            if steps < 2:
                for dr, dc in directions:
                    nr, nc = rr+dr, cc+dc
                    if 0<=nr<rows and 0<=nc<cols:
                        if (nr, nc) not in visited:
                            visited.add((nr, nc))
                            queue.append((nr, nc, steps+1))
        return result

    # Count how many cheats save >= 100
    count = 0
    for r in range(rows):
        for c in range(cols):
            if distanceS[r][c] < float('inf') and distanceE[r][c] < float('inf'):
                dA = distanceS[r][c]
                # Find up to 2-step ignoring walls from (r, c)
                neighbors = two_step_ignore_walls(r, c)
                for (rb, cb, costAB) in neighbors:
                    # Must end on track
                    if grid[rb][cb] != '#':
                        dB = distanceE[rb][cb]
                        if dB < float('inf'):
                            cheatDist = dA + costAB + dB
                            saving = normalDist - cheatDist
                            if saving >= 100:
                                count += 1
    return count

def main():
    with open('day_20/test_input.txt','r') as f:
        raw = f.read().splitlines()
    grid = [list(line) for line in raw]
    answer = solve_race_condition(grid)
    print(answer)

if __name__ == "__main__":
    main()
