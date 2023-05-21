#!/usr/bin/python3
import os
from enemies_class import Enemies
from player_class import Player

player = Player()
enemies = Enemies()
def game():
	salir=False
	while not salir:
		pinfo="player info"
		print("-"*len(pinfo))
		print("PLAYER INFO")
		print("-"*len(pinfo))
		player.show_info()
		print("-"*len(pinfo))
		print("ENEMEY INFO")
		print("-"*len(pinfo))
		enemies.show_info()
		print("-"*len(pinfo))

		opc = input("Que quieres hacer (atacar/guardar): ")
		if opc.lower() == "atacar":
			damage = player.attack()
			dead = enemies.hurt(damage)
			if not dead:
				print("El enemigo te ataca")
				edamage = enemies.attack()
				dead = player.hurt(edamage)
				if dead:
					print("Has muerto")
					print("-"*len(pinfo))
					print("PLAYER INFO")
					print("-"*len(pinfo))
					player.show_info()
					print("-"*len(pinfo))
					break
			os.system("clear")

		elif opc.lower() == "guardar":
			guardado = input("Lo quieres guardar en json o xml?(json/xml)")
			if guardado.lower() == "xml":
				player.write_info()
				enemies.write_info()
			else:
				player.write_info_js()
				enemies.write_info_js()
			break
		else:
			print("Pues atacas")
			damage = player.attack()
			dead = enemies.hurt(damage)
			if not dead:
				print("El enemigo te ataca")
				edamage=enemies.attack()
				player.hurt(edamage)
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
		if opc=="2":
			opc2=input("En que formato, xml o json?(xml/json)")
			if opc2.lower()=="xml":
				player.read_info()
				enemies.load_info()
			
			elif opc2.lower()=="json":
				player.read_info_js()
				enemies.load_info_js()
				guardado=1
			else:
				print("Pues adios")
				break
		game()	
