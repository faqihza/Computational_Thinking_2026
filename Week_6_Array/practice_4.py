# Min Max Value
# find min and max value

# Declaration:
# numbers = [-1,3,4,5,9,-5,-4,0,10,2]

numbers = [-1,3,4,5,9,-5,-4,11,10,2]

highest = 0

for number in numbers:
	# compare each step (number) with current highest
	if number > highest:
		highest = number

print(highest)

lowest = 0

for number in numbers:
	# compare each step (number) with current lowest
	if number < lowest:
		lowest = number

print(lowest)