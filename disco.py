import pygame, time
from DiscoLight import DiscoLight
from DiscoLight import DiscoLightController

pygame.init()
screen = pygame.display.set_mode([800,600])

WHITE = (255,255,255)
BLACK = (0,0,0)
GREEN = (0,255,0)
RED = (255,0,0)

discoLightsTop = [
  DiscoLight( 50,50,screen),
  DiscoLight(150,50,screen),
  DiscoLight(250,50,screen),
  DiscoLight(350,50,screen),
  DiscoLight(450,50,screen)
]

discoLightsBottom = [
  DiscoLight( 50,150,screen),
  DiscoLight(150,150,screen),
  DiscoLight(250,150,screen),
  DiscoLight(350,150,screen),
  DiscoLight(450,150,screen)
]
 
def flipScreenAndWait():
  pygame.display.flip()
  time.sleep(0.5)
  screen.fill(BLACK)

discoLightControllerTop = DiscoLightController(discoLightsTop, RED)
discoLightControllerBottom = DiscoLightController(discoLightsBottom, GREEN)

while True:
  flipScreenAndWait()
  discoLightControllerTop.setOn();
  
  flipScreenAndWait()
  discoLightControllerBottom.setOn();
