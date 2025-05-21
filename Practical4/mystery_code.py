# What does this piece of code do?
# Answer: This Python code calculates the number of attempts required to generate two identical random integers within a specified range, which is between 1 and 6. 
# Import libraries
# randint allows drawing a random number
from random import randint

# ceil takes the ceiling of a number, which is the next higher integer. For example, ceil(4.2)=5
from math import ceil

progress=0
while progress>=0:
	progress+=1
	first_n = randint(1,6)
	second_n = randint(1,6)
	if first_n == second_n:
		print(progress)
		break

