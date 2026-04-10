# entities.py

class Vector:
    """Handles the X and Y positions and movement speeds."""
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

class Player:
    """The main GitHub Explorer character."""
    def __init__(self, x, y):
        # Position and Movement Fields
        self.pos = Vector(x, y)
        self.velocity = Vector(0, 0)
        self.symbol = "웃"
        
        # --- GITHUB EXPLORER FIELDS ---
        self.repo_power = 1.8     # Jump strength (Higher = Jump higher)
        self.commit_stamina = 100 # Energy for moving/jumping
        self.stars = 0            # Your exploration score
        self.branch_level = 1     # Current world depth
        self.is_grounded = False  # True if touching the grass
        self.inventory = []       # Collected items from trees

class Tree:
    """Interactive scenery in the grassy field."""
    def __init__(self, x, y):
        self.pos = Vector(x, y)
        self.symbol = "♣"    # The leaves
        self.trunk = "║"     # The trunk
        self.has_stars = True # Can you harvest stars from this tree?

class Cloud:
    """Decorative background field elements."""
    def __init__(self, x, y):
        self.pos = Vector(x, y)
        self.symbol = "☁☁☁"
