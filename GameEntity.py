
TYPE_MALE = 0
TYPE_FEMALE = 1
TYPE_WOLF = 2
TYPE_BARRIER = 3

TYPE_LIST = [
    TYPE_MALE,
    TYPE_FEMALE,
    TYPE_WOLF,
    TYPE_BARRIER,
]

MAX_HEALTH = 100

# AI func
# def func(vision: GameMap)
#   return `action`

class GameEntity:

    def __init__(self, type: int, health:int =MAX_HEALTH):
        self.type = type
        self.health = health

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

    def damage(self, ammnt:int = 10):
        self.health = self.health - ammnt

if __name__ == "__main__":
    ge = GameEntity(TYPE_MALE)
    print(ge)