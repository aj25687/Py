import random
import time
import os

ROWS = 30
COLS = 30
INFECTION_CHANCE = 0.3  
RECOVERY_TIME = 4       
DAYS_TO_SIMULATE = 200  

grid = [[0 for _ in range(COLS)] for _ in range(ROWS)]

grid[int(ROWS/2)][int(COLS/2)] = 1 

def count_infected_neighbors(current_grid, r, c):
    count = 0
    for dr in [-1, 0, 1]:
        for dc in [-1, 0, 1]:
            if dr == 0 and dc == 0: continue 
            
            nr, nc = r + dr, c + dc
            if 0 <= nr < ROWS and 0 <= nc < COLS:
                if 1 <= current_grid[nr][nc] <= RECOVERY_TIME:
                    count += 1
    return count

for day in range(DAYS_TO_SIMULATE):
    to_infect = []
    
    current_sick = 0
    total_immune = 0
    total_healthy = 0

    for r in range(ROWS):
        for c in range(COLS):
            status = grid[r][c]
            
            if status == 0:
                total_healthy += 1
                if count_infected_neighbors(grid, r, c) > 0:
                    if random.random() < INFECTION_CHANCE:
                        to_infect.append((r, c))
            
            elif 1 <= status <= RECOVERY_TIME: 
                current_sick += 1
                grid[r][c] += 1 
                
            elif status > RECOVERY_TIME: 
                total_immune += 1

   
    for r, c in to_infect:
        grid[r][c] = 1

    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n" * 2) 
    print(f"--- DAY {day} ---")
    for row in grid:
        display_line = ""
        for cell in row:
            if cell == 0: display_line += ". "     
            elif cell <= RECOVERY_TIME: display_line += "X " 
            else: display_line += "* "           
        print(display_line)

    print(f"Healthy: {total_healthy} | Sick: {current_sick} | Immune: {total_immune}")
    
    time.sleep(0.5) 

    if current_sick == 0 and day > 0:
        print(f"\nOutbreak contained in {day} days. No more active cases.")
        break