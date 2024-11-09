#Faça um programa que aba e reproduza o áudio de um arquivo MP3.

import pygame

pygame.init()
pygame.mixer.init()

pygame.mixer.music.load('waitaminute.mp3')
pygame.mixer.music.play()
pygame.event.wait()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)