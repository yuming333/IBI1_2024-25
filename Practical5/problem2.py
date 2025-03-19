import matplotlib.pyplot as plt

# Step 1: store	the	population sizes for the UK countries and Chian provinces in two lists
uk_countries = [57.11, 3.13, 1.91, 5.45]  # England, Wales, Northern Ireland, Scotland
china_provinces = [65.77, 41.88, 45.28, 61.27, 85.15]  # Zhejiang, Fujian, Jiangxi, Anhui, Jiangsu

# Step 2: print	the	sorted	lists
sorted_uk = sorted(uk_countries)
sorted_china = sorted(china_provinces)
print("Sorted UK Country Populations (millions):", sorted_uk)
print("Sorted Zhejiang-Neighbouring Province Populations (millions):", sorted_china)

# Step 3: Create pie charts
# Labels for the pie charts
uk_labels = ["England", "Wales", "Northern Ireland", "Scotland"]
china_labels = ["Zhejiang", "Fujian", "Jiangxi", "Anhui", "Jiangsu"]


# Draw UK pie chart
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)  # Subplot for UK
plt.pie(uk_countries, labels=uk_labels, autopct='%1.1f%%', startangle=90, shadow=True)
plt.title('Population Distribution in UK Countries')

# Draw China pie chart
plt.subplot(1, 2, 2)  # Subplot for China
plt.pie(china_provinces, labels=china_labels, autopct='%1.1f%%', startangle=90, shadow=True)
plt.title('Population Distribution in Zhejiang-Neighbouring Provinces')

# Adjust layout and display the plots
plt.tight_layout()
plt.show()
