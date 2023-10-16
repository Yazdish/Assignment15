import random
from typing import Optional
import arcade
from arcade import Texture

class Fruit(arcade.Sprite):
    def __init__(self, game):
        super().__init__()
        self.width = 32
        self.height = 32
        self.center_x = random.randint(10, game.width - 10)
        self.center_y = random.randint(10, game.height - 10)
        self.change_x = 0
        self.change_y = 0

class Apple(Fruit):
    def __init__(self):
        super().__init__("apple.png")
        self.value = 1

class Pear(Fruit):
    def __init__(self):
        super().__init__("pear.png")
        self.value = 2

class Poop(Fruit):
    def __init__(self):
        super().__init__("poop.png")
        self.value = -1