# Import the necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

# Parameters
N = 10000  # Total population
beta = 0.3  # Infection rate
gamma = 0.05  # Recovery rate
days = 1000  # Simulation duration

# Vaccination rates from 0% to 100% in 10% increments
vac = np.linspace(0, 1, 11)

plt.figure(figsize=(10, 6))
colors = cm.viridis(np.linspace(0, 1, len(vac)))

for i, v_rate in enumerate(vac):
    # Initial conditions
    vaccinated = int(N * v_rate)
    S = N - vaccinated - 1  # Susceptible
    I = 1  # Initial infected
    R = vaccinated  # Vaccinated are considered recovered
    
    # Track infections over time
    infections = [I]
    
    for t in range(days):
        # Ensure non-negative values
        S = max(0, S)
        I = max(0, I)
        
        # Calculate new infections
        p_infection = beta * I / N
        if S > 0:
            new_infections = np.random.choice([0, 1], S, p=[1-p_infection, p_infection]).sum()
        else:
            new_infections = 0
        
        # Calculate new recoveries
        if I > 0:
            new_recoveries = np.random.choice([0, 1], I, p=[1-gamma, gamma]).sum()
        else:
            new_recoveries = 0
        
        # Update compartments
        S -= new_infections
        I += new_infections - new_recoveries
        R += new_recoveries
        
        infections.append(I)
    
    # Plot infection curve
    plt.plot(range(days+1), infections, color=colors[i], label=f'{int(v_rate*100)}%')

# Format plot
plt.title('SIR model with different vaccination rates', fontsize=14)
plt.xlabel('Time', fontsize=12)
plt.ylabel('Number of infected people', fontsize=12)
plt.ylim(0, 5000)
plt.xlim(0, 1000)
plt.grid(True, alpha=0.3)
plt.legend(ncol=2, title='Vaccination rate', bbox_to_anchor=(0.5, -0.15), loc='center')
plt.tight_layout()
plt.show()

