import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.animation import FuncAnimation

# Parameters
beta = 0.3  # Infection probability
gamma = 0.05  # Recovery probability
size = 100  # Grid size (100x100)
timesteps = 100  # Number of time steps to simulate

# Initialize population grid (0=susceptible, 1=infected, 2=recovered)
population = np.zeros((size, size), dtype=int)

# Randomly select patient zero
outbreak = np.random.choice(range(size), 2)
population[outbreak[0], outbreak[1]] = 1

# Create figure for visualization
plt.figure(figsize=(8, 6))
plt.title("2D Spatial SIR Model")
plt.xlabel("X Position")
plt.ylabel("Y Position")

# Define colormap: susceptible=purple, infected=blue-green, recovered=yellow
cmap = cm.colors.ListedColormap(['purple', 'cyan', 'yellow'])
bounds = [0, 1, 2, 3]
norm = cm.colors.BoundaryNorm(bounds, cmap.N)

# Function to find all infected cells
def find_infected(grid):
    return np.argwhere(grid == 1)

# Function to infect neighbors
def infect_neighbors(grid, infected_cells):
    new_grid = grid.copy()
    for cell in infected_cells:
        x, y = cell
        # Check all 8 neighbors
        for i in range(max(0, x-1), min(size, x+2)):
            for j in range(max(0, y-1), min(size, y+2)):
                if (i != x or j != y) and grid[i, j] == 0:  # Don't infect self and only susceptible
                    if np.random.random() < beta:
                        new_grid[i, j] = 1
    return new_grid

# Function to recover infected cells
def recover_cells(grid, infected_cells):
    new_grid = grid.copy()
    for cell in infected_cells:
        if np.random.random() < gamma:
            new_grid[cell[0], cell[1]] = 2
    return new_grid

# Main simulation loop
for t in range(timesteps):
    # Find all infected cells
    infected_cells = find_infected(population)
    
    # Infect neighbors
    population = infect_neighbors(population, infected_cells)
    
    # Recover infected cells
    population = recover_cells(population, infected_cells)
    
    # Plot current state
    plt.clf()
    plt.imshow(population, cmap=cmap, norm=norm, interpolation='nearest')
    plt.title(f"2D Spatial SIR Model - Time Step {t}")
    plt.xlabel("X Position")
    plt.ylabel("Y Position")
    plt.colorbar(ticks=[0.5, 1.5, 2.5], label='State', 
                 boundaries=bounds, values=[0, 1, 2])
    plt.pause(0.1)  # Pause to see the plot

plt.show()