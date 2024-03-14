class VacuumCleaner:
    def __init__(self, grid):
        self.grid, self.pos = grid, (0, 0)

    def move(self, direction):
        moves = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
        new_pos = (self.pos[0] + moves[direction][0], self.pos[1] + moves[direction][1])
        if all(0 <= coord < len(self.grid) for coord in new_pos):
            self.pos = new_pos

    def clean(self):
        if self.grid[self.pos[0]][self.pos[1]] == 1:
            print(f"Cleaning cell at {self.pos}")
            self.grid[self.pos[0]][self.pos[1]] = 0
        else:
            print(f"Cell at {self.pos} is already clean.")

    def clean_all_cells(self):
        while any(1 in row for row in self.grid):
            self.clean()
            self.move("right" if self.pos[0] % 2 == 0 and self.pos[1] < len(self.grid[0]) - 1 else "down")
            self.move("left" if self.pos[0] % 2 == 1 and self.pos[1] > 0 else "down")


# Example usage:
grid_example = [
    [1, 0, 1, 0, 1],
    [0, 1, 0, 1, 0],
    [1, 1, 1, 0, 1],
    [0, 0, 0, 1, 0],
]

vacuum = VacuumCleaner(grid_example)
vacuum.clean_all_cells()
