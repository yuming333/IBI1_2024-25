# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Define the initial basic variables of the IRS model
N = 1000 # Population size
S = N-1 # Number of sceptible people, since only one person is infected at the very beginning
I = 1 # One person is infected at the very beginning
R = 0 # Recovered individuals. Nobody has yet recovered.

beta = 0.3  # Infection rate
gamma = 0.05  # Recovery rate

# Create arrays for each of the variables to track how they evolve overtime.
S_arr = [S] 
I_arr = [I]
R_arr = [R]

# Time loop: 
# Calculate the probility of infection
# Randomly choose individuals to become infected
# Randomly choose individuals to recover
# Update the number of individuals in each variable
# Record each state in the arrays by adding the updated data using "append"
for t in range(1000):
    p_infection = beta*(I/N)
    