import random

ROWS, COLS = 10, 10
grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]
grid[5][5] = 1  
INFECTION_CHANCE = 0.4

def count_infected_neighbors(grid, r, c):
    count = 0
    for ir in [-1, 0, 1]:
        for ic in [-1, 0, 1]:
            if ir == 0 and ic == 0:
                continue
            neighbor_r = r + ir
            neighbor_c = c + ic
            if 0 <= neighbor_r < len(grid) and 0 <= neighbor_c < len(grid[0]):
                if grid[neighbor_r][neighbor_c] == 1:
                    count += 1
    return count

for day in range(10):
    to_infect = [] 

    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 0:
                neighbors = count_infected_neighbors(grid, r, c)
                
                if neighbors > 0:
                    if random.random() < INFECTION_CHANCE:
                        to_infect.append((r, c))

    for r, c in to_infect:
        grid[r][c] = 1

    print(f"Day {day}: {len(to_infect)} new infections.")



n_count = count_infected_neighbors(grid, 2, 1)

print(f"(2,1) has {n_count} infected neighbor(s).")
