# Faça um programa em py que abra e reproduza um audio em MP3
import pygame
pygame.init() #inicializa o PyGame

pygame.mixer.music.load('Exe021.mp3') #Le o arquivo.
pygame.mixer.music.play() #Executa a musica
pygame.event.wait() #Somente sai do programa ao terminar a MP3.
