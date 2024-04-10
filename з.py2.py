from pygame import *

'''Классы'''
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_s] and self.rect.x < win_width - 85:
            self.rect.x += self.speed


''' Окно'''
W, H = 600, 500
window = display.set_mode((W, H))
display.set_caption('Пинг Понг')
back = (3, 250, 245)
window.fill(back)
'''Игровой таймер'''
clock = time.Clock()
FPS = 60 
'''Игровой цикл'''
game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        display.update()
        clock.tick(FPS)
