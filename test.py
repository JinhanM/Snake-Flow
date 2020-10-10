from pygame import *
import pygame
import random


mindist = 20
size = 13
dist = size * mindist + 100
fields = []
gen = 0
snakes = []
# stolbK = int((WIDTH + 100) / dist)
# print(stolbK)




# My variables
WIDTH = 1000
HEIGHT = 900

grids = (5, 5)
grid_size = 40

RIGHT = [1, 0]
LEFT = [-1, 0]
UP = [0, -1]
DOWN = [0, 1]
moves = {K_UP: UP, K_DOWN: DOWN, K_RIGHT: RIGHT, K_LEFT: LEFT}




class Field:
    def __init__(self):
        self.dist = dist
        self.mindist = mindist

    def draw(self, sc):
        for x in range(grids[0]+1):
            pygame.draw.line(sc, (0, 0, 0), (0+grid_size*x, 0), (0+grid_size*x, grid_size*grids[1]))
        for y in range(grids[1]+1):
            pygame.draw.line(sc, (0, 0, 0), (0, 0+grid_size*y), (grid_size*grids[1], 0+grid_size*y))




class Snake:
    def __init__(self):
        self.body = []
        self.empty_grid = [[i, j] for i in range(grids[0]) for j in range(grids[1])]
        self.food = None
        self.last_move = [1, 0]
        self.create_body()
        self.create_food()
        self.timenoeat = 0

    def create_food(self):
        self.food = self.empty_grid[random.randint(0, len(self.empty_grid)-1)]
        self.empty_grid.remove(self.food)

    def create_body(self):
        self.body = [self.empty_grid[0], self.empty_grid[1]]
        for piece in self.body:
            self.empty_grid.remove(piece)

    def check_eaten(self, move):
        return [self.body[0][0] + move[0], self.body[0][1] + move[1]] == self.food

    def check_legit_move(self):
        next_head = [self.body[0][0] + self.last_move[0], self.body[0][1] + self.last_move[1]]
        return not (next_head[0] < 0 or next_head[1] < 0 or next_head[0] > grids[0]-1 or next_head[1] > grids[1]-1 or
                    next_head in self.body)

    def move(self):
        if self.check_legit_move():
            # 检查有没有吃到
            if self.check_eaten(self.last_move):
                self.body.insert(0, self.food)
                self.create_food()
            else:
                self.empty_grid.append(self.body[-1])
                self.body.pop(-1)
                self.empty_grid.remove([self.body[0][0] + self.last_move[0], self.body[0][1] + self.last_move[1]])
                self.body.insert(0, [self.body[0][0] + self.last_move[0], self.body[0][1] + self.last_move[1]])

    def draw(self, sc):
        pygame.draw.rect(sc, (255, 0, 0), ((self.food[0]*grid_size, (self.food[1])*grid_size), (grid_size, grid_size)))
        pygame.draw.rect(sc, (0, 150, 0), ((self.body[0][0]*grid_size, self.body[0][1]*grid_size),
                         (grid_size, grid_size)))
        for body in self.body[1:]:
            pygame.draw.rect(sc, (0, 100, 0), ((body[0]*grid_size, body[1]*grid_size), (grid_size, grid_size)))

    def change_direction(self, next_move):
        self.last_move = next_move


class Game:
    def __init__(self, fields, snakes):
        self.fields = fields
        self.snakes = snakes
        self._is_playing = True

    def run(self):
        # 初始化screen
        pygame.init()
        pygame.font.init()
        clock = pygame.time.Clock()
        # STAT_FONT = pygame.font.SysFont("comicsans", 50)
        screen = pygame.display.set_mode((WIDTH, HEIGHT))
        # 游戏开始
        while self._is_playing:
            clock.tick(1)
            # 画背景
            screen.fill((255, 255, 255))
            # 画格子
            for f in self.fields:
                f.draw(screen)
            # 画蛇
            for s in self.snakes:
                s.draw(screen)

            # 键盘操作
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == K_ESCAPE:
                        pygame.quit()
                    if event.key in moves:
                        snake.change_direction(moves[event.key])
            if snake.check_legit_move():
                snake.move()
            else:
                self._is_playing = False
                print("Game Over")


if __name__ == "__main__":
    snake = Snake()
    field = Field()

    game = Game([field], [snake])
    game.run()
