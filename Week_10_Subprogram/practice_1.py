import os

def print_banner():
	os.system("clear")
	print(20*"=")
	print("ONLINE FOOD DELIVERY")
	print(20*"=")
	print("\n")

while(True):
	print_banner()

	print("Menu:")
	print("1. User Management")
	print("2. Discovery & Ordering")
	print("3. Checkout & Payment")
	print("4. Tracking & Feedback")
	print(20*"-")
	print("\n")
	item_menu_index = input("Please, select menu (1/2/3/4)? ")

	# this is submenu

	if item_menu_index == "1":
		print_banner()
		print("this is first menu")
	elif item_menu_index == "2":
		print_banner()
		print("this is second menu")
	else:
		print_banner()
		print("other menu")

	user_end = input("do you want to exit (y/n)? ")

	if user_end == "y":
		break

print("end of program")