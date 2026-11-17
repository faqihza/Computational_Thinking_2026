## sums user input

# DECLARATION:
# numbers = [0,....,N]
# result_sum


# ALGORITHM
# 1. array declaration
tabInt = [0,0,0,0,0,0,0,0,0,0]
result_sum = 0

# 2. get user input
index = 0
for i in tabInt:
	# assign user's input
	tabInt[index] = int(input("number = "))
	result_sum = result_sum + tabInt[index]

	index = index + 1

print(tabInt)

print(result_sum)

# 3. average

result_average = result_sum / len(tabInt)

print(result_average)