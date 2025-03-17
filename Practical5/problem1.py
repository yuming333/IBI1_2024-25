
language_data = {"JavaScript": 62.3,"HTML": 52.9,"Python": 51,"SQL": 51,"TypeScript": 38.5}
print(language_data)

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

languages = list(language_data.keys())
percentages = list(language_data.values())

plt.bar(languages, percentages)
plt.xlabel('Programming Language')

plt.ylabel('Percentage of Users')
plt.title('Programming Language Popularity in February 2024')
plt.show()

input_language = "Python" 
if input_language in language_data:
    print(f"The percentage of developers who use {input_language} is {language_data[input_language]}%")
else:
    print(f"{input_language} is not in the provided data.")