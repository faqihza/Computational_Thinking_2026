# numbers: int and float

user_input = input("fill a number=")
a = float(user_input)

if a > 0:
	print("This is positive")
elif a < 0:
	print("This is negative")
else:
	print("This is zero!")