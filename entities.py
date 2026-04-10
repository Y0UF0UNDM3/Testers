class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Player:
    def __init__(self, x, y):
        self.pos = Vector(x, y)
        self.velocity = Vector(0, 0)
        self.symbol = "웃"
        # --- FIELDS ---
        self.repo_power = 1.5    # How high you jump
        self.commit_stamina = 100 # Energy resource
        self.stars = 0           # Your score
        self.is_grounded = False # Touching grass?

class Tree:
    def __init__(self, x, y):
        self.pos = Vector(x, y)
        self.symbol = "♣"
        self.trunk = "║"
