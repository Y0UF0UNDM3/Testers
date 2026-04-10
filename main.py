import os
import time
from entities import Player
from world import World

def start_game():
    world = World()
    player = Player(10, 2) # Spawns in the sky to show gravity

    try:
        while True:
            world.apply_gravity(player)
            player.pos.y += player.velocity.y
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f"STARS: {player.stars} | STAMINA: {player.commit_stamina}")
            print(world.render(player))
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("\nStopped Exploring.")

if __name__ == "__main__":
    start_game()
