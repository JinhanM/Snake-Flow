import pygame

WIN_WIDTH = 800
WIN_HEIGHT = 800
n = 4
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

BG_IMG = "load background image"
SNAKE_PIXEL = "load snake pixel"


def get_grids():
    grids = []
    row = []
    for i in range(n):
        grids.append(row)
        for j in range(n):
            row.append(pixel)
    return grids


GRIDS = get_grids()


class pixel:
    def __init__(self):
        self.is_occupied = False
        self.object = None

    def add_new_item(self, item):
        self.is_occupied = True
        self.object = item

    def remove_item(self, item):
        self.is_occupied = False
        self.object = item

class snake:
    def __init__(self):
        self.is_head = True
        self.is


# class snake:
#
#     def __init__(self):
#         self.pixel = SNAKE_PIXEL
#         self.position = []
#         self.direction = "U"
#
#     def get_head_pos(self):
#         return self.position[0]
#
#     def move(self):
#         if self.position == "U":
#             self.position.append(self.position[0])
#             self.position[-1][1] += 1
#         if self.position == "D":
#             self.position.append(self.position[0])
#             self.position[-1][1] -= 1
#         if self.position == "R":
#             self.position.append(self.position[0])
#             self.position[-1][0] += 1
#         if self.position == "L":
#             self.position.append(self.position[0])
#             self.position[-1][1] -= 1

