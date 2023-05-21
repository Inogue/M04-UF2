#!/usr/bin/python3
import xmltodict
import random
import json

class Enemy:
	def __init__ (self, name, health, strength, description = ""):
		self.name = name
		self.health = int(health)
		self.strength = strength
		self.description = description
		
		print(self.name+": "+self.description)
	
	def attack (self):
		return random.randint(0,int(self.strength))
	def hurt (self, damage):
		if int(self.health) > 0:
			self.health-=damage
			return False
		if int(self.health) <= 0:
			return True
	
	def write_info_js(self):
		info1={
		"name": self.name,
		"health": self.health,
		"damage": self.strength,
		"description": self.description
		}
		enemy_info1 ={
		"enemies":{
		"enemy": info1
		}
		}
		with open("enemy_save.json", "w") as e:
			json.dump(enemy_info1, e)

	def write_info(self):
		info1={
		"name": self.name,
		"health": self.health,
		"damage": self.strength,
		"description": self.description
		}
		enemy_info1 = {
		"enemies": {
		"enemy": info1
			}
		}
		xml_file = open("enemy_save_xml", "w")
		xml_file.write(xmltodict.unparse(enemy_info1))
		xml_file.close()
	
	def load_info_js (self):
		with open("enemy_save.json") as e:
			data = json.load(e)
		info1=data["enemies"]["enemy"]
		self.name=str(info1["name"])
		self.health=int(info1["health"])
		self.damage=int(info1["damage"])
		self.description=str(info1["description"])

	def load_info (self):
		xml_file=open("enemy_save_xml", "r")
		enemy_tmp=xmltodict.parse(xml_file.read())
		xml_file.close()
		info1=enemy_tmp['enemies']['enemy']
		self.name=str(info1["name"])
		self.health=int(info1["health"])
		self.damage=int(info1["damage"])
		self.description=str(info1["description"])

	def show_info (self):
		print("Name "+(self.name))
		print("Health "+str(self.health))
		print("Strength "+str(self.strength))
		if self.description != "":
			print("Description"+(self.description))


if __name__ == "__main__":

	enemigo = Enemy("Jacinto", 33, 10, "Simplemente Jacinto"); 
	
	enemigo.show_info()
	print(enemigo.hurt(enemigo.attack()))
	enemigo.show_info()
