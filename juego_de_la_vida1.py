import pygame

pygame.init()

ventana_x = 800
ventana_y = 800
ventana = pygame.display.set_mode((ventana_x,ventana_y))

estado_actual = []

lista_auxiliar = []

ejecucion = True
cantidad_celdas = 40
pausa = False

longitud_celda = 20

for y in range(cantidad_celdas):
	for x in range(cantidad_celdas):

		lista_auxiliar.append(0)
	estado_actual.append(lista_auxiliar)
	
	lista_auxiliar = []

tiempo = pygame.time.Clock()
while ejecucion:

	ventana.fill((0,0,0))

	tiempo.tick(60)

	if not pausa:
	
		suma = 0

		estado_futuro = []

		for y in range(len(estado_actual)):
			
			celda = ()
			for x in range(len(estado_actual[y])):

				celda = (estado_actual[(y+1) % cantidad_celdas][x % cantidad_celdas],
				estado_actual[(y+1) % cantidad_celdas][(x+1) % cantidad_celdas],
				estado_actual[(y+1) % cantidad_celdas][(x-1) % cantidad_celdas],
				estado_actual[y % cantidad_celdas][(x+1) % cantidad_celdas],
				estado_actual[y % cantidad_celdas][(x-1) % cantidad_celdas],
				estado_actual[(y-1) % cantidad_celdas][(x+1) % cantidad_celdas],
				estado_actual[(y-1) % cantidad_celdas][(x-1) % cantidad_celdas],
				estado_actual[(y-1) % cantidad_celdas][x % cantidad_celdas])

				suma = sum(celda)
				
				if estado_actual[y][x]:

					if suma == 2 or suma == 3:

						lista_auxiliar.append(1)
					else:
						lista_auxiliar.append(0)
				else:
					if suma == 3:

						lista_auxiliar.append(1)
					else:
						lista_auxiliar.append(0)

				celda = ()
			estado_futuro.append(lista_auxiliar)
			lista_auxiliar = []

		estado_actual = estado_futuro

		lista_auxiliar = []

	raton = pygame.mouse.get_pos()
	raton_teclas = pygame.mouse.get_pressed()

	if raton_teclas[0]:

		celdaraton_x = raton[0] // longitud_celda
		celdaraton_y = raton[1] // longitud_celda

		estado_actual[celdaraton_y][celdaraton_x] = 1

	elif raton_teclas[2]:

		celdaraton_x = raton[0] // longitud_celda
		celdaraton_y = raton[1] // longitud_celda

		estado_actual[celdaraton_y][celdaraton_x] = 0 

	for y in range(len(estado_actual)):

			for x in range(len(estado_actual[y])):

				color = (255,255,255)

				if estado_actual[y][x]:
					pygame.draw.rect(ventana,color,[x*longitud_celda,y*longitud_celda,longitud_celda,longitud_celda])
				else:       
					pygame.draw.rect(ventana,color,[x*longitud_celda,y*longitud_celda,longitud_celda,longitud_celda],1)
		
	for i in pygame.event.get():

		if i.type == pygame.QUIT:
			ejecucion = False

		if i.type == pygame.KEYDOWN:
			if i.key == pygame.K_p:
				pausa = not pausa

	pygame.display.update()