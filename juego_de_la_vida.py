import pygame
import time
import numpy

class Escenario():
	ar = []
	ar_2 = []

	def __init__(self,n,ventana):				
		self.n = n		
		self.ventana = ventana
		self.ar = self.crear_cuadrantes()
		self.ar = tuple(self.ar)		
		
	def crear_cuadrantes(self):
		ar = []
		for i in range(self.n):
			ar.append([])
			for j in range(self.n):
				
				ar[i].append(0)
		return ar

	def dibujar(self):
		x = 0
		y = 0
		blanco = (255,255,255)
		negro = (0,0,0)
		color = ()
		self.ar_2 = self.crear_cuadrantes() 
		for i in range(len(self.ar)):			
			for j in range(len(self.ar[i])):
			
				if self.ar[i][j] == 0:
					color = negro
				else:
					color = blanco		
					
				x = j * self.n
				y = i * self.n

				ar3 = [[x+1,y+1],[x+self.n-1,y+1],[x+self.n-1,y+self.n-1],[x+1,y+self.n-1]]
				pygame.draw.polygon(self.ventana,color,ar3)

				x1,y1,valor = self.reglas(j,i)
				self.ar_2[y1][x1] = valor
			
		self.ar = self.ar_2
		self.ar_2 = []
	

	def coordenas_raton(self):
		x,y = pygame.mouse.get_pos()
		botones = pygame.mouse.get_pressed()		
		x = x // self.n
		y = y // self.n		
		if botones[0] == 1:			
			self.ar[y][x] = 1
			x *= self.n
			y *= self.n
			ar3 = [[x+1,y+1],[x+self.n-1,y+1],[x+self.n-1,y+self.n-1],[x+1,y+self.n-1]]
			pygame.draw.polygon(self.ventana,(255,255,255),ar3) 		
		elif botones[2] == 1:
			self.ar[y][x] = 0
			x *= self.n
			y *= self.n
			ar3 = [[x+1,y+1],[x+self.n-1,y+1],[x+self.n-1,y+self.n-1],[x+1,y+self.n-1]]
			pygame.draw.polygon(self.ventana,(0,0,0),ar3) 	

	def reglas(self,x,y):
		
		valor = 0
		
		v = (self.ar[y%self.n][(x+1)%self.n],
				self.ar[y%self.n][(x-1)%self.n],
				self.ar[(y+1)%self.n][x%self.n],
				self.ar[(y-1)%self.n][x%self.n],
				self.ar[(y-1)%self.n][(x+1)%self.n],
				self.ar[(y-1)%self.n][(x-1)%self.n],
				self.ar[(y+1)%self.n][(x+1)%self.n],
				self.ar[(y+1)%self.n][(x-1)%self.n])				
		v = sum(v)
		if self.ar[y][x] == 0:
			if v == 3:
				valor = 1			
		if self.ar[y][x] == 1:
			if v < 2 or v > 3:
				valor = 0
			else:
				valor = 1

		return x,y,valor
		
class Ventana():

	def __init__(self):
		self.x = 677
		self.y = 677
		self.ventana = pygame.display.set_mode((self.x,self.y))
		self.ejecutar = True
		self.pausa = False
		self.e = Escenario(26,self.ventana)

	def ciclo(self):		
		
		clock = pygame.time.Clock()
		while self.ejecutar:			

			self.e.coordenas_raton()
			if not self.pausa:
				self.ventana.fill((255,255,255))
				self.e.dibujar()
			for i in pygame.event.get():
				if i.type == pygame.QUIT:
					self.ejecutar = False
				elif i.type == pygame.KEYDOWN:
					if i.key == pygame.K_p:
						self.pausa = not self.pausa	
			clock.tick(10)
			pygame.display.update()
v = Ventana()
v.ciclo()