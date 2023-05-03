#!/usr/bin/python3

import xmltodict
from enemy_class import Enemy

class Enemies:
	def __init__(self):
		xml_file = open("enemy_xml", "r")
		enemies_tmp = xmltodict.parse(xml_file.read())
		
		enemies_list = enemies_tmp['enemies']['enemy']
		
		self.enemies_count=0		
		self.enemies = []
		for e in enemies_list:
			 self.enemies.append(Enemy(e["name"], e["health"], e["damage"], " TE"))
	def show_info(self):
		self.enemies[self.enemies_count].show_info()
	def attack(self):
		return self.enemies[self.enemies_count].attack()
	def hurt(self, damage):
		dead = self.enemies[self.enemies_count].hurt(damage)
		if dead:
			print("Lo mataste mamahuevo")
			self.enemies_count += 1
			return True
		return False
	
if __name__ == "__main__":
	enemies = Enemies()
