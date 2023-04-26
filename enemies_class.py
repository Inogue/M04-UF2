#!/usr/bin/python3

import xmltodict
from enemy_class import Enemy

class Enemies:
	def __init__(self):
		xml_file = open("enemy_xml", "r")
		enemies_tmp = xmltodict.parse(xml_file.read())
		
		enemies_list = enemies_tmp['enemies']['ememy']
	
		for e in enemies_list:
			tmp = Enemy(e["name"], e["health"], e["strength"], "TE")

if __name__ == "__main__":
	enemies = Enemies()
