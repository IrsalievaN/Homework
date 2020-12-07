string = "Happy birthday"

for letter in string:
	if letter == "a":
		continue
	elif letter == "n":
		print( "HA-HA")
		break 
	else:
		print(string)
else:
	print("Congratulations!!!")
