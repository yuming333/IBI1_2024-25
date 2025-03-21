# Use an empty list to store the data
triangle_numbers = []
# Loop from 1 to 10 to calculate the first ten values
for n in range(1, 11):
# Initialize the sum of the current triangular number
    sum = 0
# Loop from 1 to n to calculate the sum from 1 to n
    for i in range(1, n + 1):
        sum += i
    triangle_numbers.append(sum)# Add the calculated sum to the list

# Print each triangular number
for number in triangle_numbers:
     print(number)
