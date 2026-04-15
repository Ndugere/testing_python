from collections import deque 

def number_of_islands(grid: list) -> int:
    if not grid:
        return 0
    
    rows, cols  = len(grid), len(grid[0])
    visited, islands = set(), 0

    def bfs(r,c):
        queue = deque([(r,c)])
        visited.add((r,c))
        while queue:
            x, y = queue.popleft()
            directions = [(-1, 0), (1, 0), (0, -1), (0,1)]
            for dr, dc in directions:
                row, col = x + dr, y + dc
                if (0 <= row < rows) and (0 <= col < cols) and ((row, col) not in visited) and (str(grid[row][col]) == 1):
                    queue.append((row, col))
                    visited.add((row, col))


    for r in range(rows):
        for c in range(cols):
            if str(grid[r][c]) == "1" and (r, c) not in visited:
                bfs(r,c)
                islands += 1
    
    return islands

