# Maze Generation using DFS
# A small maze is created using Depth-First Search.

import random

ROWS = 5
COLS = 5


def generate_maze(rows, cols):
    # Each cell starts with all four walls present.
    maze = [[{"N": 1, "S": 1, "E": 1, "W": 1}
             for _ in range(cols)] for _ in range(rows)]
    visited = [[False] * cols for _ in range(rows)]

    directions = [
        (-1, 0, "N", "S"),
        (1, 0, "S", "N"),
        (0, 1, "E", "W"),
        (0, -1, "W", "E")
    ]

    def dfs(row, col):
        visited[row][col] = True
        random.shuffle(directions)

        for dr, dc, wall, opposite in directions:
            nr, nc = row + dr, col + dc

            if (0 <= nr < rows and 0 <= nc < cols
                    and not visited[nr][nc]):
                maze[row][col][wall] = 0
                maze[nr][nc][opposite] = 0
                dfs(nr, nc)

    dfs(0, 0)
    return maze


def print_maze(maze):
    rows = len(maze)
    cols = len(maze[0])

    # Top boundary
    print("+" + "---+" * cols)

    for r in range(rows):
        line = "|"
        bottom = "+"
        for c in range(cols):
            line += "    " if maze[r][c]["E"] == 0 else "   |"
            bottom += "   +" if maze[r][c]["S"] == 0 else "---+"
        print(line)
        print(bottom)


random.seed(7)  # Fixed seed so the sample maze is repeatable
maze = generate_maze(ROWS, COLS)

print("MAZE GENERATION USING DFS")
print(f"Grid size: {ROWS} x {COLS}")
print("Start: top-left   Finish: bottom-right")
print_maze(maze)
