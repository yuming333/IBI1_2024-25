# dalys.py

# Import neccessary libraries
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Change path and read the file
os.chdir("C:/Users/wym/Desktop/wym/IBI1_2024-25/Practical10")
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

# Get some basic  information about dalys_data
dalys_data.info()

# Showing the year for the first 10 rows
years_first_10_rows = dalys_data.iloc[:10, 2]
print(years_first_10_rows)
# Comment: The 10th year with DALYs data recorded in Afghanistan is 1999

# Show DALYs for all countries in 1990 using a Boolean
dalys_1990 = dalys_data.loc[dalys_data.Year == 1990, "DALYs"]
print(dalys_1990)

# Compute the mean DALYs in the UK and France.
dalys_uk = dalys_data.loc[dalys_data.Entity == "United Kingdom", "DALYs"].mean()
dalys_france = dalys_data.loc[dalys_data['Entity'] == 'France', 'DALYs'].mean()
print(f"Mean DALYs in UK: {dalys_uk}, Mean DALYs in France: {dalys_france}")
if dalys_uk > dalys_france:
    print("Mean DALYs in UK is greater than in France")
else:
    print("Mean DALYs in UK is smaller than in France")
# Comment: Mean DALYs in UK is greater than in France    


# Create a plot showing the DALYS over time in the UK
uk = dalys_data.loc[dalys_data.Entity=="United Kingdom", ["DALYs", "Year"]]
plt.figure(figsize=(10, 6))
plt.plot(uk.Year, uk.DALYs, "b+")
plt.xticks(rotation=-45) # Rotate the x ticks to make them being shown clearly and separatedly.
plt.xlabel('Year')
plt.ylabel('DALYs')
plt.title('DALYs Over Time in the UK')
plt.show()

# Aswer the question: What country or countries have recorded a DALYs greater than 650,000 in a single year?
countries_over_650k = dalys_data[dalys_data['DALYs'] > 650000] 
countries_over_650k_entities = countries_over_650k['Entity'].unique() # Integrate the same things
print("Countries with DALYs > 650,000 in a single year:", countries_over_650k_entities.tolist()) # Clear display as Python list
