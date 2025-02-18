import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    timer = pygame.time.Clock()

    print("Starting asteroids!")
    print("Screen width:" , SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots ,updatable, drawable)

    main_player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    rand_asteroids = AsteroidField()
    dt = 0

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            

        updatable.update(dt)
        for obj in asteroids:
            if obj.collision(main_player):
                print("Game Over")
                font = pygame.font.Font(None, 74)
                text = font.render("Game Over", True, (255, 0, 0),"aquamarine4")
                screen.blit(text, (SCREEN_WIDTH//2 - text.get_width()//2, SCREEN_HEIGHT//2 - text.get_height()//2))
                pygame.display.flip()
                pygame.time.wait(1000)
                return 
            for obj2 in shots:
                if obj2.collision(obj):
                    obj.split()
                    obj2.kill()
        screen.fill("black")
        
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        dt = timer.tick(60)/1000
        

if __name__ == "__main__":
    main()