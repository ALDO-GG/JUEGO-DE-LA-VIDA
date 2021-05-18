import pygame

ventana = pygame.display.set_mode((600,600))
ejecutar = True

estato_actual = []
longitud_celdas = 20
pausa = False
cantidad_celdas = 30

for y in range(30):
	ar = []
	for x in range(30):
		ar.append([0])
	estato_actual.append(ar)

def dibujar():

	for y in range(len(estato_actual)):
		for x in range(len(estato_actual[y])):

			if estato_actual[y][x] == 1:
				pygame.draw.rect(ventana,(255,255,255),[x*longitud_celdas,y*longitud_celdas,longitud_celdas,longitud_celdas])
			else:
				pygame.draw.rect(ventana,(255,255,255),[x*longitud_celdas,y*longitud_celdas,longitud_celdas,longitud_celdas],1)

def selecionar():

	raton_posicion = pygame.mouse.get_pos()
	raton_teclas = pygame.mouse.get_pressed()

	if raton_teclas[0]:

		x = raton_posicion[0] // longitud_celdas
		y = raton_posicion[1] // longitud_celdas

		estato_actual[y][x] = 1

	if raton_teclas[2]:

		x = raton_posicion[0] // longitud_celdas
		y = raton_posicion[1] // longitud_celdas

		estato_actual[y][x] = 0

def reglas():
	global estato_actual

	estado_futuro = []
	for y in range(30):
		ar = []
		for x in range(30):
			ar.append([0])
		estado_futuro.append(ar)

	for y in range(len(estato_actual)):
		for x in range(len(estato_actual[y])):
			celda = (estato_actual[y%cantidad_celdas][(x+1)%cantidad_celdas],
					estato_actual[y%cantidad_celdas][(x-1)%cantidad_celdas],
					estato_actual[(y+1)%cantidad_celdas][x%cantidad_celdas],
					estato_actual[(y+1)%cantidad_celdas][(x+1)%cantidad_celdas],
					estato_actual[(y+1)%cantidad_celdas][(x-1)%cantidad_celdas],
					estato_actual[(y-1)%cantidad_celdas][x%cantidad_celdas],
					estato_actual[(y-1)%cantidad_celdas][(x-1)%cantidad_celdas],
					estato_actual[(y-1)%cantidad_celdas][(x+1)%cantidad_celdas])
			celda = celda.count(1)

			if estato_actual[y][x] == 1:
				if celda > 1 and celda < 4:
					estado_futuro[y][x] = 1
				else: 
					estado_futuro[y][x] = 0
			else:
				if celda == 3:
					estado_futuro[y][x] = 1
	estato_actual = estado_futuro

tiempo = pygame.time.Clock()
while ejecutar:

	tiempo.tick(30)
	
	ventana.fill((0,0,0))
	selecionar()
	dibujar()
	if not pausa:
		reglas()

	for i in pygame.event.get():
		if i.type == pygame.QUIT:
			ejecutar = False
		if i.type == pygame.KEYDOWN:
			if i.key == pygame.K_ESCAPE:
				ejecutar = False
			if i.key == pygame.K_p:
				pausa = not pausa

	pygame.display.update()