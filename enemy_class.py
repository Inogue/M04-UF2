#!/usr/bin/python3

class Enemy:
	def __init__ (self, name, health, strength, description):
		self.name = name
		self.health = health
		self.strength = strength
		self.description = description
		
		print(self.name+": "+slef.description)

if __name__ == "__main__":

	enemigo = Enemy("Jacinto", 33, 10, "Simplemente Jacinto"); 
