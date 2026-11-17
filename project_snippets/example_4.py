username = "ucup"
password = "ucup"

is_login = False
while True:
	print("1 - Login")
	print("2 - regis")
	print("3 - exit")

	user_pick = input("pick menu: ")
	if user_pick == "1":
		username_input = input("username : ")
		password_input = input("password : ")

		if (username == username_input) and (password == password_input):
			is_login = True
			break

		print("wrong password")
		user_enter = input("go back to login page")
	elif user_pick == "2":
		print("user_registration")
		user_enter = input("go back to login page")
	elif user_pick == "3":
		break


if is_login:
	print("next program")

print("end of the program")