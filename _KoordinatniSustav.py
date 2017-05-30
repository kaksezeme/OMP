import pygame
from pygame.locals import *

from _Tocka import Tocka


CRNA = (0, 0, 0)
BIJELA = (255, 255, 255)
PLAVA = (0, 0, 255)
CRVENA = (224, 6, 6)
ZELENA = (0, 250, 0)


class KoordinatniSustav:
    iscrtavaj = True
    PROZOR = None
    duzine = None
    '''1024 x 750 zoom 50'''
    '''1920 x 180 zoom 80'''

    zoom = 25
    sirina = 800
    visina = 600
    izvor = Tocka(sirina / 2, visina / 2)

    def __init__(self, duzine):
        pygame.init()
        self.PROZOR = pygame.display.set_mode((self.sirina, self.visina), 0, 32)
        pygame.display.set_caption('Koordinatni sustav')
        self.duzine = duzine
        self.prikazi_prozor()

    def postavi_koordinatni_sustav(self):
        self.PROZOR.fill(BIJELA)
        pygame.draw.line(self.PROZOR, CRNA, (0, self.visina / 2), (self.sirina, self.visina / 2), 3)
        pygame.draw.line(self.PROZOR, CRNA, (self.sirina / 2, 0), (self.sirina / 2, self.visina), 3)
        i = self.kalibritaj_velicinu(Tocka(1, 0))
        j = self.kalibritaj_velicinu(Tocka(0, 1))
        pygame.draw.line(self.PROZOR, ZELENA, (self.izvor.x, self.izvor.y), (self.izvor.x + i.x, self.izvor.y + i.y), 3)
        pygame.draw.line(self.PROZOR, ZELENA, (self.izvor.x, self.izvor.y), (self.izvor.x + j.x, self.izvor.y + j.y), 3)

    def kalibritaj_velicinu(self, tocka):
        return Tocka(tocka.x * self.zoom, -(tocka.y * self.zoom))

    def crtaj_liniju(self, t1, t2, boja):
        t1 = self.kalibritaj_velicinu(t1)
        t2 = self.kalibritaj_velicinu(t2)

        pygame.draw.line(self.PROZOR, boja, (self.izvor.x + t1.x, self.izvor.y + t1.y),
                         (self.izvor.x + t2.x, self.izvor.y + t2.y), 4)

    def prikazi_prozor(self):
        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
            if self.iscrtavaj:
                self.postavi_koordinatni_sustav()
                i = 0
                for x in self.duzine:
                    if i / 2 == 0:
                        self.crtaj_liniju(x.a, x.b, CRVENA)
                    else:
                        self.crtaj_liniju(x.a, x.b, PLAVA)
                    i = i + 1
                self.iscrtavaj = False
            pygame.display.update()
