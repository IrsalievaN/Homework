import lab1

slots = self.slots - 1

dragon_attacks = []
a = 0
while hp_dragon > 0:
	if slots >= 0:
		dragon_perk_damage = hero.perk()

		else:
		dragon_damage = hero.attack()

	a = a + 1
	dragon_attacks.append(a)

	hp_dragon = hp - dragon_damage - dragon_perk_damage 
	dragon_average_damage  = (dragon_damage + dragon_perk_damage) / hero_attacks 
else:
	print(death()) 

hero_attacks = []
i = 0
while hp_hero > 0:
	if slots >=0:
		hero_perk_damage = dragon.perk()

	else:
		hero_damage = dragon.attack()

	i = i + 1	
	hero_attacks.append(a)

	hp_hero = hp - hero_damage - hero_perk_damage
	hero_average_attacks = (hero_damage + hero_perk_damage) / dragon_attacks

else:
	print(death())

