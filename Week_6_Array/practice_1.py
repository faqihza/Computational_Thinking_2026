## Program PopulatingArray
# Populating an array with 
# values ​​from the user 

# DECLARATIONS
# tabInt : array [0..9] of int
# i : int

# ALGORITHM 

# 1. declare the variables
# array of 10

tabInt = [0,0,0,0,0,0,0,0,0,0]
# tabInt = list(range(0,10))


# 2. get user input
index = 0
for i in tabInt:
	print("index - ",index)
	# assign user's input
	tabInt[index] = int(input("number = "))

	index = index + 1

	print(tabInt)

# 3. print the final array

print(tabInt)