#!/usr/bin/python3

from enemies_class import Enemies
from player_class import Player

player = Player()
enemies = Enemies()
def game():
	salir=False
	while not salir:
		print("Te ataca un enemigo")
		enemies.show_info()

		opc = input("Que quieres hacer (atacar/guardar): ")
		if opc == "atacar":
			damage = player.attack()
			dead = enemies.hurt(damage)
			if not dead:
				print("El enemigo te ataca")
				damage = enemies.attack()
				player.hurt(damage)

if __name__ == "__main__":
	title="Empiesa el juego"
	print(title)
	print("-"*len(title))

	opc = ""
	while opc!="s":
		print("1.- Juego nuevo")
		print("2.- Cargar juego")
		print("S.- Salir")

		opc= input("Introduce una opcion ").lower()

		if opc=="1":
			player.input_info()
			
			player.write_info()

		if opc=="2":
			player.read_info()
			player.show_info()
		game()	
