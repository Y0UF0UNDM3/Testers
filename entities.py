# entities.py

class Vector:
    """Handles movement and positioning."""
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Player:
    """The Explorer navigating the field."""
    def __init__(self, x, y):
        # Position and Movement
        self.pos = Vector(x, y)
        self.velocity = Vector(0, 0)
        self.symbol = "웃"
        
        # --- EXPLORER FIELDS ---
        self.repo_power = 1.8     # Jump height/Physics strength
        self.commit_stamina = 100 # How far you can sprint/explore
        self.exploration_rank = 1 # Increases as you find new areas
        self.is_grounded = False  # Physics check for gravity
        self.view_distance = 15   # How much of the 'codebase' you can see

class Tree:
    """Natural landmarks in the world."""
    def __init__(self, x, y):
        self.pos = Vector(x, y)
        self.symbol = "♣"    # Leaves
        self.trunk = "║"     # Trunk
        self.type = "Ancient" # Just lore/description

class Landmark:
    """Special points of interest to find."""
    def __init__(self, x, y, name, icon):
        self.pos = Vector(x, y)
        self.name = name
        self.icon = icon
