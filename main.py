import os,pygame,sys
from CONST import *
from car import *

class Game():

    def __init__(self):
        pygame.init()

        self.load_txt()
        self.load_sounds()

        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.draw_screen = pygame.Surface(SCREEN_SIZE)
        self.clock = pygame.time.Clock()
        self.dt = 1


        self.game()

    def game(self):

        self.car = Car()

        while True:
            self.check_keys()
            self.check_events()
            self.draw()
            self.refresh_screen()



    def load_txt(self):
        self.textures = {}
        for img in os.listdir("img"):
            texture = pygame.image.load("img/" + img)
            self.textures[img.replace(".png", "")] = texture

    def load_sounds(self):
        self.sounds = {}
        for sound in os.listdir("sounds"):
            file = pygame.mixer.Sound("sounds/" + sound)
            self.sounds[sound.replace(".wav", "")] = file

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.close()


    def check_keys(self):
       pass

    def draw(self):
        self.draw_screen.blit(self.textures["background"],(0,0))
        self.draw_screen.blit(self.textures["car"], self.car)


    def refresh_screen(self):
        scaled = pygame.transform.scale(self.draw_screen, SCREEN_SIZE)
        for i in (0,2):
            self.screen.blit(scaled,(i*650,0))
        pygame.display.update()
        self.dt = self.clock.tick(FRAMERATE) * FRAMERATE / 1000

    def close(self):
        pygame.quit()
        sys.exit(0)

Game()