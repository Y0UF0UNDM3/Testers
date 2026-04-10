# world.py
import random
from entities import Tree

class World:
    def __init__(self, width=80, height=20):
        self.width = width
        self.height = height
        self.gravity = 0.5
        self.ground_level = height - 4
        self.entities = []
        self.generate_world()

    def generate_world(self):
        self.trees = [Tree(random.randint(5, self.width-10), self.ground_level - 1) for _ in range(8)]
        # Add random decorative elements
        self.clouds = [(random.randint(2, self.width-10), random.randint(1, 4)) for _ in range(3)]
        self.mountains = [(random.randint(0, self.width-15), self.ground_level) for _ in range(2)]

    def apply_gravity(self, player):
        # Check if above ground level
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
                
                # 1. Background Layer: Clouds
                for cx, cy in self.clouds:
                    if y == cy and x in range(cx, cx+5): char = "☁"
                
                # 2. Midground Layer: Mountains
                for mx, my in self.mountains:
                    if y == my - 1 and x == mx + 2: char = "^"
                    if y == my - 2 and x == mx + 2: char = "A"

                # 3. Ground Layer: Soil and Grass
                if y > self.ground_level: char = "▒" # Soil depth
                elif y == self.ground_level: char = "░" # Grassy surface
                
                # 4. Scenery Layer: Trees and Houses
                for t in self.trees:
                    if x == int(t.pos.x) and y == int(t.pos.y): char = t.symbol
                    if x == int(t.pos.x) and y == int(t.pos.y) + 1: char = t.trunk

                # 5. Entity Layer: Player
                if x == int(player.pos.x) and y == int(player.pos.y):
                    char = player.symbol
                
                row.append(char)
            screen.append("".join(row))
        
        # Add a water pool at the far right
        final_render = "\n".join(screen)
        return final_render
