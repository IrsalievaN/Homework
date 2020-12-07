'''
import random

while True:
	command = input(">>> ")
	phrases = ["Никто не ценит того, чего слишком много.","Где нет опасности, не может быть и славы.","Сердце можно лечить только сердцем.","Красотой спасётся мир","Каждый день имеет своё чудо."]

	if command == "Скажи мудрость":
		print(random.choice(phrases))
	elif command == "Знать ничего не хочу":
		print("Okay(((")
		continue
	elif command == "Выход":
		print("До свидания")
		break
	else:
		print("Неверный ввод")

'''

print(eval("1+1+1+2"))
