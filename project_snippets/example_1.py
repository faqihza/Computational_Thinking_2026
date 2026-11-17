merchant = ["Bu Rara","Pak Dadang","Mbak Sinta"]
menus = [["pizza", "donut", "rice bowl", "bread", "sourdough"],
         ["Nasi Goreng","mie Goreng"],
	 ["sate ayam","sate kambing"]]

for i in range(len(merchant)):
	print(f"Welcome to - {merchant[i]}")
	for j in range(len(menus[i])):
		print(f"{j+1} - {menus[i][j]}")
