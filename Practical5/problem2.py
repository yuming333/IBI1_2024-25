try:
    import matplotlib.pyplot as plt
except ModuleNotFoundError:         # Increase the fault - tolerance rate to prevent the program from malfunctioning in case matplotlib is not properly installed.
    print("The matplotlib library is not installed.")

# Step 1: Create lists for population data
uk_countries = [57.11, 3.13, 1.91, 5.45]  # England, Wales, Northern Ireland, Scotland
china_provinces = [65.77, 41.88, 45.28, 61.27, 85.15]  # Zhejiang, Fujian, Jiangxi, Anhui, Jiangsu

# Step 2: Sort the lists and print them
sorted_uk = sorted(uk_countries)
sorted_china = sorted(china_provinces)

print("Sorted UK Country Populations (millions):", sorted_uk)
print("Sorted Zhejiang-Neighbouring Province Populations (millions):", sorted_china)

# Step 3: Create pie charts
# Labels for the pie charts
uk_labels = ["England", "Wales", "Northern Ireland", "Scotland"]
china_labels = ["Zhejiang", "Fujian", "Jiangxi", "Anhui", "Jiangsu"]

# Customize pie charts
colors_uk = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']  # Custom colors for UK pie chart
colors_china = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#c2c2f0']  # Custom colors for China pie chart
explode_uk = (0.1, 0, 0, 0)  # Highlight England in the UK pie chart
explode_china = (0.1, 0, 0, 0, 0)  # Highlight Zhejiang in the China pie chart

# Draw UK pie chart
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)  # Subplot for UK
plt.pie(uk_countries, labels=uk_labels, autopct='%1.1f%%', colors=colors_uk, explode=explode_uk, startangle=90, shadow=True)
plt.title('Population Distribution in UK Countries')

# Draw China pie chart
plt.subplot(1, 2, 2)  # Subplot for China
plt.pie(china_provinces, labels=china_labels, autopct='%1.1f%%', colors=colors_china, explode=explode_china, startangle=90, shadow=True)
plt.title('Population Distribution in Zhejiang-Neighbouring Provinces')

# Adjust layout and display the plots
plt.tight_layout()
plt.show()
