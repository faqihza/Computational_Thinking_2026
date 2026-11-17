## Summing All Members
# this program is to get the sum of an array

# DECLARATION:
# numbers = [0,....,N]
# result_sum

# ALGORITHM

# 1. set of array

numbers = [0,2,4,6,8,10]
result_sum = 0

# 2. summing
for number in numbers:
	result_sum = result_sum + number

print(result_sum)

# 3. average

result_average = result_sum / len(numbers)

print(result_average)