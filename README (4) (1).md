# Maze Generation using DFS

A beginner-friendly Python project that creates a maze using Depth-First Search (DFS).

## How it works
- The maze is a 5 × 5 grid.
- Every cell starts with four walls.
- DFS visits an unvisited neighboring cell, removes the wall between the cells, and continues deeper.
- When there are no unvisited neighbors, DFS backtracks.
- The result is a maze with a path connecting all cells.

## Run
```bash
python maze_generation.py
```

No external libraries are required; `random` is included with Python.

## Concepts used
- Depth-First Search (DFS)
- Recursion and backtracking
- 2D lists and grid neighbors
- Randomized maze generation

## Note
The program uses a fixed random seed so the displayed sample maze is repeatable. Change or remove `random.seed(7)` to generate a different maze each run.
