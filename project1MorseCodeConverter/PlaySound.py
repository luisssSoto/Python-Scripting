from pathlib import Path
import pygame
import time

short_beep = Path(__file__).parent / "assets" / "short_beep.mp3"
long_beep = Path(__file__).parent / "assets" / "long_beep.mp3"

pygame.mixer.init()

class PlaySound:
    def __init__(self, code_morse):
        self.code_morse = code_morse
    
    def play_code_morse(self):
        '''Play a "beep" according the morse code symbol'''
        for letter in self.code_morse:
            for symbol in letter:
                if symbol == '.':
                    print(symbol)
                    pygame.mixer.Sound(short_beep).play()
                    pygame.time.wait(300)
                elif symbol == '-':
                    print(symbol)
                    pygame.mixer.Sound(long_beep).play()
                    pygame.time.wait(1200)
                elif symbol == '/':
                    time.sleep(.5)
            time.sleep(.25)
        

