import random


class Pirate:

    def __init__(self, name):
        self.name = name
        self.strength = 10
        self.speed = 3
        self.health = 100
        self.rum = 1

    def show_stats(self):
        print(
            f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack(self, ninja):
        crit_chance = random.randint(1, 20)
        if crit_chance < self.speed:
            damage = self.strength * 2
            ninja.health -= damage
            print(f"{self.name} is SO fast! He did double damage!")
        else:
            damage = self.strength
            ninja.health -= damage
        print(
            f"{self.name} swings his cutlass and does {damage} damage\n {ninja.name} has {ninja.health} health left!")

    def drink_rum(self):
        if self.rum > 0:
            print(f"{self.name} takes a swig of rum! + 5 Strength, - 10 Health..")
            self.rum -= 1
            self.speed += 1
            self.strength += 5
            self.health -= 10
            print(f"There are {self.rum} swigs left")
        else:
            print(f"{self.name} tries to take another drink... Misses his mouth!")
