import pygame

class music():
    def __init__(self,file='') -> None:
        pygame.mixer.init()
        if file != '':
            self.file = file
    def play(self):
        pygame.mixer.music.load(self.file)
        self.music = pygame.mixer.music.play(-1)
        return self.music
    def pause()->None:
        pygame.mixer.music.pause()
    def start()->None:
        pygame.mixer.music.unpause()
    def end()->None:
        pygame.mixer.music.stop()

