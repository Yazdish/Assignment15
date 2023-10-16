
import arcade
from fruit import Apple
from fruit import Pear
from fruit import Poop
from snake import Snake

class Game(arcade.Window):
    def __init__(self):
        super().__init__(width = 500 , height = 500 , title = "Super Snake 🐍 V.01")
        arcade.set_background_color(arcade.color.KHAKI)
        self.snake = Snake(self)
        self.food1 = Apple(self)
        self.food2 = Pear(self)
        self.food3 = Poop(self)

    def on_draw(self):
        arcade.start_render()
        
        self.snake.draw()
        self.food1.draw()
        self.food2.draw()
        self.food3.draw()
        
        arcade.finish_render()    

    def on_update(self):
        self.snake.move()

        if arcade.check_for_collision(self.snake, self.food1):
            self.snake.eat(self.food1)
            self.food1 = Apple(self)

        if arcade.check_for_collision(self.snake, self.food2):
            self.snake.eat(self.food2)
            self.food2 = Pear(self)

        if arcade.check_for_collision(self.snake, self.food3):
            self.snake.eat(self.food3)
            self.food3 = Poop(self)

        # arcade.draw_text(self.snake.score, 10, 20, arcade.color.BLACK, 20)
    
    
    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.UP:
            self.snake.change_x = 0
            self.snake.change_y = 1

        elif symbol == arcade.key.DOWN:
            self.snake.change_x = 0
            self.snake.change_y = -1

        elif symbol == arcade.key.RIGHT:
            self.snake.change_x = 1
            self.snake.change_y = 0

        elif symbol == arcade.key.LEFT:
            self.snake.change_x = -1
            self.snake.change_y = 0




if __name__ == "__main__":
    game = Game()
    arcade.run()

