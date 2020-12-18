from abc import ABC, abstractmethod
import math
import random

strength = 8
dexterity = 8
constitution = 8
intelligence = 8
wisdom = 8
charisma = 8

class Character(ABC):
	
	def attack(self):
		self.damage = random.randint(0, 12) + floor((strength - 10) / 2)
	
	def save_throw(self, attribute):
		self.st = random.randint(0, 20) + floor((attribute - 10) / 2)

	@abstractmethod
	def  perk(self):
		self.health = random.randint(0, 16) + floor((intelligence - 10) / 2)
		self.damage = random.randint(0, 16) + floor((intelligence - 10) / 2)

class Hero(Character):

	def perk(self):
		super().perk()

class Dragon(Character):
	def perk(self):
		self.damage = random.randint(0, 12) + floor((strength - 10) / 2)


name = input("Введите имя игрока:\n")
level = int(input("Введите уровень игрока:\n"))
h = Hero()
d = Dragon()

max_hp = 10 + floor(constitution - 10) / 2 + random.randint(0, 10) * level
print("max_hp", max_hp)
hp = max_hp
print("hp = ", hp)
armour_class = 15 +  floor(dexterity - 10) / 2
print("armour_class = ", armour_class)
initiative = random.randint(0, 20) + floor(dexterity - 10) / 2
print("initiative = ", initiative)
