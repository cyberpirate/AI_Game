
from GameAI import GameAI
from GameConstants import *

# AI func
# def func(vision: GameMap)
#   return `action`

class GameEntity:

    def __init__(self, type: int, ai:GameAI = None, health:int =MAX_HEALTH):
        self.type = type
        self.health = health
        self.ai = ai

    def __str__(self):
        if self.type == TYPE_MALE:
            return "M"
        elif self.type == TYPE_FEMALE:
            return "F"
        elif self.type == TYPE_WOLF:
            return "W"
        elif self.type == TYPE_BARRIER:
            return "B"
        else:
            return "U"

    def damage(self, ammnt:int = 50):
        self.health = self.health - ammnt

if __name__ == "__main__":
    ge = GameEntity(TYPE_MALE)
    print(ge)