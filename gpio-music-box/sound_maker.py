import pygame
from gpiozero import Button

pygame.init()

button1 = Button(17)
button2 = Button(22)
button3 = Button(5)
button4 = Button(13)

sound1 = pygame.mixer.Sound('samples/perc_snap2.wav')
sound2 = pygame.mixer.Sound('samples/perc_bell.wav')
sound3 = pygame.mixer.Sound('samples/perc_snap.wav')
sound4 = pygame.mixer.Sound('samples/ambi_piano.wav')

button1.when_pressed = sound1.play
button2.when_pressed = sound2.play
button3.when_pressed = sound3.play
button4.when_pressed = sound4.play



















































































































































































































sound3.play()
sound4.play()
