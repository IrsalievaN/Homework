def calc(a, b, c):
	if c == "+":
		return a + b
	elif c == "-":
		return a - b
	elif c == "*":
		return a * b
	elif c == "/":
		return a / b
	else:
		print("Вы ввели неправильный оператор")


while True: 
	
	a = input("Первое число: ")
	b = input("Второе число: ")
	c = input("Оператор: ")
	
	if a.isdigit() and b.isdigit():
		a = float(a)
		b = float(b)

	else:
		print("Вы ввели не число")
	
	print(calc(a, b, c))