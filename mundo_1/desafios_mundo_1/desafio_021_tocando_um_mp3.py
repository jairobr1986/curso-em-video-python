#Exercício Python 21: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
import pygame
import time

pygame.init()
#Abaixo é caminho para que funcione corretamente no linux e depois de muita pesquisa
#tive que adicionar um timer para que a musica não ficasse parando só abria e tocava
#tocava apenas 2 segundos e parava.
"""
pygame.mixer.music.load('/media/jairobr1986/ALEATORIO/jairo/curso-em-video/desafios/hey021.mp3')

"""

#abaixo é o caminho para que toque no Windows, também depois de muita pesquisa conseguir fazer funcionar
#mas enfim ficou pronto

pygame.mixer.music.load('d:/jairo/curso-em-video/desafios/hey021.mp3')


pygame.mixer.music.play()

time.sleep(5000)
pygame.mixer.music.stop()

