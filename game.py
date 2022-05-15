from random import randit
from pygame import*
font.init()
font=font.Font(None,72)
#mixer.init()
#mixer.init.load('')
#mixer.musik.play()
win_width=800
win_height=600
left_bound=win_width / 40
right_bound=win_height - 8 * left_bound
shift=0
x_start=20
y_start=10
img_file_back='bg.jpg'
img_file_hero='player.png'
img_file_enemy='sprite.png'
img_file_bomb='bomb.png'
img_file_door='dorr.png'
img_wall='wall.png'
FPS=60

C_WHITE=(255,255,255)
C_DARK=(48,48,0)
C_YELLOW=(255,255,87)
C_GREEN=(32,128,32)
C_RED=(255,0,0)
C_BLACK=(0,0,0,)

# создание врагов и мин 
en = Enemy(300,330)
all_sprites.add(en)
enemies.add(en)

bomb = Enemy(250,200, img_file_bomb, 60,60)
bombs.add(bomb)

door = FinalSprite(img_file_door, win_width + 500, win_height - 150, 0)
all_sprites.add(door)

#final sprite
class FinalSprite(sprite.Sprite):
    def __init__(self, player_image, player_x , player_y, player_speed):
        sprite.Sprite.__init__(self)

        self.image = transform.scale(image.load(player_image) , (100 ,100))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        
# в цикде пока не финиш
if not finished:
    all_sprites.update()
    sprite.groupcollide(bombs,all_sprites, True,True)
    
    if sprite.spritesollide(robin,enemies, False):
        robin.kill()
    if (
        robin.rect.x > right_bound and robin.x_speed > 0
        or
        robin.rect.x < left_bound and robin.x_speed < 0
    ):
        shift -= robin.x_speed
        for s in all_sprites:
            s.rect.x -= robin.x_speed
        for s in bombs:
            s.rect.x -= robin.x_speed
        for s in enemies:
            s.rect.x -= robin.x_speed
