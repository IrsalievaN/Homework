from stack2 import *

s = myStack()


print("Введите количество элементов в стеке")
n = int(input())

if n <= 0:
	print("Стек не может быть пустым")
else:
	print("Введите элементы")
	for i in range (n):
		element = int(input())
		s.push(element)

print(s.remove())
print(s)
print(s.is_empty())

