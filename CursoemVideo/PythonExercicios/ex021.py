import pygame
pygame.init()
som = pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
while True:
    inpt = input('Minha música com a mulher da minha vida... ')
    print(inpt)
pygame.mixer.music.wait()
