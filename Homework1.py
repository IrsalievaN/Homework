age = int(input("Введите возраст:\n"))
if 0 <= age < 18:
	print("Вы юноша")
elif 18 <= age < 45:
	print("Вы молодой")
elif 45 <= age < 60:
	print("Вы среднего возраста")
elif 60 <= age < 75:
	print("Вы пожилой")
elif 75 <= age < 90:
	print("Вы старец")
elif 90 <= age:
	print("Вы долгожитель")
else:
	print("Неправильно введен возраст")