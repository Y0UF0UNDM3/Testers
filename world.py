import random
from entities import Tree

class World:
    def __init__(self, width=60, height=15):
        self.width = width
        self.height = height
        self.gravity = 0.5       # Pulling strength field
        self.ground_level = height - 3
        self.trees = [Tree(random.randint(5, 55), self.ground_level - 1) for _ in range(6)]

    def apply_gravity(self, player):
        if player.pos.y < self.ground_level - 1:
            player.velocity.y += self.gravity
            player.is_grounded = False
        else:
            player.pos.y = self.ground_level - 1
            player.velocity.y = 0
            player.is_grounded = True

    def render(self, player):
        screen = []
        for y in range(self.height):
            row = []
            for x in range(self.width):
                char = " " 
                if y > self.ground_level: char = "▒" # Soil
                elif y == self.ground_level: char = "░" # Grass
                for t in self.trees:
                    if x == int(t.pos.x) and y == int(t.pos.y): char = t.symbol
                    if x == int(t.pos.x) and y == int(t.pos.y) + 1: char = t.trunk
                if x == int(player.pos.x) and y == int(player.pos.y): char = player.symbol
                row.append(char)
            screen.append("".join(row))
        return "\n".join(screen)
