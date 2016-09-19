import pygame

class DiscoLight:
  width = 50
  height = 50
  def __init__(self, x, y, screen):
    self.x = x
    self.y = y
    self.screen = screen
    
  def setColour(self, colour):
    #screen,                      colour,         position,            size
    pygame.draw.rect(self.screen, colour, [self.x, self.y, self.width, self.height])


class DiscoLightController:
  def __init__(self, lights, colour):
    self.lights = lights
    self.colour = colour
    
  def setOn(self):
    for light in self.lights:
      light.setColour(self.colour)
