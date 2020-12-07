import random
while True:

	phrases = ["Никто не ценит того, чего слишком много.","Где нет опасности, не может быть и славы.","Сердце можно лечить только сердцем.","Красотой спасётся мир","Каждый день имеет своё чудо."]
	phrase = input("")
	if phrase == "Скажи мне мудрость":
		print(phrases[random.randint(0, len(phrases) - 1)],)
		break

	elif phrase == "Знать ничего не хочу":
		print("Ok(((")
		continue

	elif phrase == "Выйти":
		break
	else:
		print("Неверный ввод")



