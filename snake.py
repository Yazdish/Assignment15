import arcade

class Snake(arcade.Sprite):
    def __init__(self, game):
        super().__init__()
        self.width = 32
        self.height = 32
        self.center_x = (game.width // 2)
        self.center_y = (game.height // 2)
        self.color1 = arcade.color.GREEN
        self.color2 = arcade.color.GREEN_YELLOW
        self.change_x = 0
        self.change_y = 0
        self.speed = 4
        self.score = 0
        self.body = []


    def draw(self):
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width, self.height, self.color1)

        for part in self.body:
            # if self.body[part] % 2 != 0:
            #     arcade.draw_rectangle_filled(part['x'], part['y'], self.width, self.height, self.color2)
            # elif self.body[part] % 2 == 0:
                arcade.draw_rectangle_filled(part['x'], part['y'], self.width, self.height, self.color1)


    def move(self):
        self.body.append({'x':self.center_x, 'y':self.center_y})
        if len(self.body) > self.score:
            self.body.pop(0)
    
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed



    def eat(self, food1, food2, food3):
        del food1
        self.score += 1
        del food2
        self.score += 2
        del food3
        self.score -= 1
