#final sprite
class FinalSprite(sprite.Sprite):
    def __init__(self, player_image, player_x , player_y, player_speed):
        sprite.Sprite.__init__(self)

        self.image = transform.scale(image.load(player_image) , (100 ,100))
        self.speed = player_speed

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
