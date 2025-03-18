# Dictionary to store programming language popularity
language_popularity = { "JavaScript": 62.3, "HTML": 52.9, "Python": 51, "SQL": 51, "TypeScript": 38.5 }
# Print the dictionary,so it is easy to see if the data is stored properly
print(language_popularity)

try:
    import matplotlib.pyplot as plt
except ModuleNotFoundError:         # Increase the fault - tolerance rate to prevent the program from malfunctioning in case matplotlib is not properly installed.
    print("The matplotlib library is not installed.")
    
# Get the keys and percentage data from the dictionary created above, and store the data in two separated lists.
languages = list(language_popularity.keys())
percentages = list(language_popularity.values())

# Draw a bar chart describing the data in the dictionary
plt.figure(figsize = (10,6))
plt.bar(languages,percentages,color='skyblue') 
plt.xlabel('Programming Languages') # Add x axis's label 
plt.ylabel('Percentage of Users') # Add y axis's label
plt.title('Programming Language Popularity in February 2024') # Add title of the bar chart
plt.show() # Display the bar chart

input_language = "Python" # Pick a kind of language from the given chart.A variable	of the requested activity that can be modified.
# Print the result
if input_language in language_popularity:
    print(f"The percentage of developers who use {input_language} is {language_popularity[input_language]}%")
else:
    print(f"{input_language} is not in the provided data.")


