# Bus commute
a = 15  # Time needed to walk to the bus stop in minutes
b = 75  # Time spent on taking the bus in minutes (1 hour and 15 minutes)
c = a + b  # Total bus commute time

# Car commute
d = 90  # Drive time in minutes (1 hour and 30 minutes)
e = 5   # Walk time from the car park in minutes
f = d + e  # Total car commute time

# Compare c and f, and get a result.
if c < f:
    result = "The bus commute is quicker."
elif c > f:
    result = "The car commute is quicker."
else:
    result = "Both commutes take the same amount of time."

# Record the result
# The bus commute takes 90 minutes, and the car commute takes 95 minutes.
# Therefore, the bus commute is quicker.
print(result)



# Initialize Boolean variables
X = True
Y = False

# Compute 'both X and Y'
W = X and Y

# Truth table for W:
# X      Y      W
# Ture   Ture   Ture
# Ture   False  Ture
# False  Ture   False
# False  False  False



