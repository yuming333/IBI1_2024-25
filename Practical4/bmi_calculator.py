# Step 1: Get the weight (in kg) and height (in m) of the person

# Step 2: Calculate the BMI using the formula: BMI = weight / (height ** 2)

# Step 3: Determine the category based on BMI(using "if,elif,else"):
# - BMI < 18.5: Underweight
# - 18.5 <= BMI <= 30: Normal weight
# - BMI > 30: Obese

# Step 4: Print the result, which includes the BMI and category
# BMI Calculator


# Step 1
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))


# Step 2
bmi = round(weight / (height ** 2), 2)


# Step 3
if bmi < 18.5:
    category = "underweight"
elif 18.5 <= bmi <= 30:
    category = "normal weight"
else:
    category = "obese"

# Step 4
print("Your BMI is " + str(bmi) + ", which means you are " + category + ".")
