stuff = ["racket","ball","shoes"]
price = [200000,100000,500000]
stock = [3,4,6]

order = []

while True:
	for i in range(len(stuff)):
		print(f"{i+1} - {stuff[i]}")

	print(f"current order - {order}")
	user_input = int(input("pick your stuff number? "))
	
	if user_input == 0:
		break

	order.append(user_input)

print(f"final order = {order}")

sum_price = 0
for i in order:
	price_stuff = price[i-1]
	sum_price = sum_price + price_stuff

print(f"final price = {sum_price}")