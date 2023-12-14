import pygame

class Boton():
	def __init__(self, x, y, imagen, scale):
		width = imagen.get_width()
		height = imagen.get_height()
		self.imagen = pygame.transform.scale(imagen, (int(width * scale), int(height * scale)))
		self.rect = self.imagen.get_rect()
		self.rect.topleft = (x, y)
		self.presiono = False

	def dibujar_y_verificar(self, pantalla):
		accion = False
		posicion_mouse = pygame.mouse.get_pos()

		if self.rect.collidepoint(posicion_mouse):
			if pygame.mouse.get_pressed()[0] == 1 and self.presiono == False:
				self.presiono = True
				accion = True

		if pygame.mouse.get_pressed()[0] == 0:
			self.presiono = False

		pantalla.blit(self.imagen, (self.rect.x, self.rect.y))

		return accion