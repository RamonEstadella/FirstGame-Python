# IMPORTS
import pygame # Para crear el juego
import sys # Para cerrar el programa
import random # Para generar números aleatorios

#Constantes
ANCHO = 800 # Dimension de la ventana del juego
ALTO = 600 # Dimension de la ventana del juego
color_rojo = (255,0,0) # Color en formato RGB
color_negro = (0,0,0) # Color en formato RGB
color_azul = (0,0,255) # Color en formato RGB

#Jugador
jugador_size = 50 # Define el Tamaño del jugador
jugador_pos = [ANCHO / 2, ALTO - jugador_size * 2] # Definimos la posición inicial del jugador

#Enemigo(s)
enemigo_size = 50 # Define el Tamaño del jugador enemigo
enemigo_pos = [random.randint(0,ANCHO - enemigo_size),0] # Posición inicial enemigo
# La posición horizontal del enemigo es aleatoria dentro de los límites de la ventana, 
# y empieza en la parte superior.

#ventana
ventana = pygame.display.set_mode((ANCHO,ALTO)) # Inicializamos la ventana del juego

game_over = False # Es una Bandera que indica si el jugo ha terminado
clock = pygame.time.Clock() # Se usa para controlar la velocidad del juego

#Funcion para comprobar si el jugador ha colisionado con el enemigo
# La función compara las posiciones del jugador y del enemigo y devuelve True si hay colisión.
def detectar_colision(jugador_pos,enemigo_pos):
	jx = jugador_pos[0]
	jy = jugador_pos[1]
	ex = enemigo_pos[0]
	ey = enemigo_pos[1]

	if (ex >= jx and ex <(jx + jugador_size)) or (jx >= ex and jx < (ex + enemigo_size)):
		if (ey >= jy and ey <(jy + jugador_size)) or (jy >= ey and jy < (ey + enemigo_size)):
			return True
		return False


# Iniciamos el bucle principal del juego que se ejecutará mientras 'game_over' sea 'False'
while not game_over: 

	# Procesamos los eventos que ocurren en la ventana del juego. 
	# Si se cierra la ventana, el juego termina.
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	# Procesamos las pulsaciones de teclas para mover el jugador a la izquierda o a la derecha. 
	# Actualizamos la posición horizontal del jugador en consecuencia.
		if event.type == pygame.KEYDOWN:
			x = jugador_pos[0]
			if event.key == pygame.K_LEFT:
				x -= jugador_size
			if event.key == pygame.K_RIGHT:
				x += jugador_size

			jugador_pos[0] = x

	# Llenamos la ventana con el color negro para limpiar la pantalla antes de dibujar 
	# los nuevos elementos. 		
	ventana.fill(color_negro)


	# Movemos al enemigo hacia abajo. Si el enemigo alcanza el borde inferior de la ventana, 
	# se reposiciona aleatoriamente en la parte superior.
	if enemigo_pos[1] >= 0 and enemigo_pos[1] < ALTO:
		enemigo_pos[1] += 20
	else:
		enemigo_pos[0] = random.randint(0,ANCHO - enemigo_size)
		enemigo_pos[1] = 0


	#Colisiones

	# Comprobamos si hay una colisión entre el jugador y el enemigo utilizando la función 
	# detectar_colision. Si hay colisión, game_over se establece en True, terminando el juego.
	if detectar_colision(jugador_pos,enemigo_pos):
		game_over = True

	# Dibujar enemigo
	# Dibujamos al enemigo en la ventana usando las coordenadas y el tamaño del enemigo.
	pygame.draw.rect(ventana, color_azul,
			(enemigo_pos[0],enemigo_pos[1],
			enemigo_size, enemigo_size))
	

	#Dibujar jugador
	pygame.draw.rect(ventana, color_rojo,
			(jugador_pos[0],jugador_pos[1],
			jugador_size,jugador_size))
	
	# Controlamos la velocidad del juego, limitando el bucle principal a 30 iteraciones por segundo.
	clock.tick(30)

	# Actualizamos la pantalla para mostrar los nuevos dibujos del jugador y el enemigo.
	pygame.display.update()
