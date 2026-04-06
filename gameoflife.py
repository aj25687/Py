rows = 5
cols = 5
grid = [[0 for _ in range(cols)] for _ in range(rows)]
#1=infected
#0=safe
grid[2][2] = 1

def count_infected_neighbors(grid, r, c):
    count = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0:
                continue
            neighbor_r = r + dr
            neighbor_c = c + dc
            if 0 <= neighbor_r < len(grid) and 0 <= neighbor_c < len(grid[0]):
                if grid[neighbor_r][neighbor_c] == 1:
                    count += 1
    return count

n_count = count_infected_neighbors(grid, 2, 1)

print(f"(2,1) has {n_count} infected neighbor(s).")
