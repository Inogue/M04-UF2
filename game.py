
#!/usr/bin/python3
import xmltodict
import os
import random	
from enemy_class import Enemy
from player_class import Player

nombre = input("Como te llamas? ")
os.system("clear")

enemy_files = "enemy_xml"

print("BIENVENIDO "+(nombre)+" A NUESTRO JUEGO")

with open(enemy_files, "r") as f:
	xml_string = f.read()

enemy_dict = xmltodict.parse(xml_string)

def select_enemy (number):
	name = str(enemy_dict["enemies"]["enemy"][number]["name"])
	description =str(enemy_dict["enemies"]["enemy"][number]["description"])
	health = int(enemy_dict["enemies"]["enemy"][number]["health"])
	strength = int(enemy_dict["enemies"]["enemy"][number]["damage"])
	print(name)
	print(description)
	print(health)
	print(strength)

player_health = 20
initial_player_health= player_health

while True:
	player = Player(nombre)
	attack = jugador.attack(10)
	enemy = Enemy()
	emey_attack = enemy.attack(strength)
	level = player.get_level(xp)
	xp=0
	numero = 0
	juego = select_enemy(numero)	
	action = input("¿Qué quieres hacer? (ataca/nothing)")

	if action == "ataca":
		print(f"Has quitado {ataque} puntos de vida al enemigo.")
	else:
		print("Espabila que te matan")

	player_health -= enemy_attack
	print(f"El enemigo te ha quitado {enemy_attack} puntos de vida.")

	if (health <= 0) and (numero>len(enemy_dict)) :
		print("Acabaste con él. ¡Felicidades!")
		xp = random.radiant(1, level)*initial_player_health
		print(level)
		break
    
	if player_health <= 0:
		print("Mala suerte papu, has perdido.")
		break
	numero=numero+1
	select_enemy(numero)
