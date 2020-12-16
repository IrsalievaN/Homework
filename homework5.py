from abc import ABC, abstractmethod
from math import pi

class Figure(ABC):
	@abstractmethod
	def draw (self):
		print("Квадрат нарисован")

class Round(Figure):
	def draw(self):
		print("Круг нарисован")


	def __square(a):
		return S = a ** 2 * pi

class Square(Figure):
	def draw(self):
		super().draw()

	@staticmethod
	def square(a):
		return S = a ** 2

a = int(input("Введите а:\n"))

r = Round()
s = Square()
print()
r.draw()
print()
s.draw()
print()
print(s.square(a))

print(r._Round__square())
