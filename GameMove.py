
from GameMap import GameMap

MOVE_RIGHT = 0
MOVE_DOWN = 1
MOVE_LEFT = 2
MOVE_UP = 3

ATTACK_RIGHT = 4
ATTACK_DOWN = 5
ATTACK_LEFT = 6
ATTACK_UP = 7

DO_NOTHING = 8

ACTION_LIST = [
    MOVE_RIGHT,
    MOVE_DOWN,
    MOVE_LEFT,
    MOVE_UP,
    ATTACK_RIGHT,
    ATTACK_DOWN,
    ATTACK_LEFT,
    ATTACK_UP,
    DO_NOTHING,
]

ACTION_NAMES = {
    MOVE_RIGHT: "MOVE_RIGHT",
    MOVE_DOWN: "MOVE_DOWN",
    MOVE_LEFT: "MOVE_LEFT",
    MOVE_UP: "MOVE_UP",
    ATTACK_RIGHT: "ATTACK_RIGHT",
    ATTACK_DOWN: "ATTACK_DOWN",
    ATTACK_LEFT: "ATTACK_LEFT",
    ATTACK_UP: "ATTACK_UP",
    DO_NOTHING: "DO_NOTHING",
}

def moveRight(gm: GameMap, pos: (int, int)):

    dest = (pos[0] + 1, pos[1])

    if pos[0] >= gm.size or pos[1] >= gm.size:
        return False
    if pos[0] < 0 or pos[1] < 0:
        return False

    if dest[0] >= gm.size or dest[1] >= gm.size:
        return False
    if dest[0] < 0 or dest[1] < 0:
        return False

    if gm.data[dest] != None:
        return False
    
    gm.data[dest] = gm.data[pos]
    gm.data[pos] = None
    return True

def moveDown(gm: GameMap, pos: (int, int)):
    dest = (pos[0], pos[1] + 1)

    if pos[0] >= gm.size or pos[1] >= gm.size:
        return False
    if pos[0] < 0 or pos[1] < 0:
        return False

    if dest[0] >= gm.size or dest[1] >= gm.size:
        return False
    if dest[0] < 0 or dest[1] < 0:
        return False
    
    if gm.data[dest] != None:
        return False

    gm.data[dest] = gm.data[pos]
    gm.data[pos] = None
    return True

def moveLeft(gm: GameMap, pos: (int, int)):
    dest = (pos[0] - 1, pos[1])

    if pos[0] >= gm.size or pos[1] >= gm.size:
        return False
    if pos[0] < 0 or pos[1] < 0:
        return False

    if dest[0] >= gm.size or dest[1] >= gm.size:
        return False
    if dest[0] < 0 or dest[1] < 0:
        return False
        
    if gm.data[dest] != None:
        return False
        
    gm.data[dest] = gm.data[pos]
    gm.data[pos] = None
    return True

def moveUp(gm: GameMap, pos: (int, int)):
    dest = (pos[0], pos[1] - 1)

    if pos[0] >= gm.size or pos[1] >= gm.size:
        return False
    if pos[0] < 0 or pos[1] < 0:
        return False

    if dest[0] >= gm.size or dest[1] >= gm.size:
        return False
    if dest[0] < 0 or dest[1] < 0:
        return False
        
    if gm.data[dest] != None:
        return False
        
    gm.data[dest] = gm.data[pos]
    gm.data[pos] = None
    return True

def attackRight(gm: GameMap, pos: (int, int)):

    dest = (pos[0] + 1, pos[1])

    if pos[0] >= gm.size or pos[1] >= gm.size:
        return False
    if pos[0] < 0 or pos[1] < 0:
        return False

    if dest[0] >= gm.size or dest[1] >= gm.size:
        return False
    if dest[0] < 0 or dest[1] < 0:
        return False

    if gm.data[dest] is None:
        return False
    
    gm.data[dest].damage()
    return True

def attackDown(gm: GameMap, pos: (int, int)):
    dest = (pos[0], pos[1] + 1)

    if pos[0] >= gm.size or pos[1] >= gm.size:
        return False
    if pos[0] < 0 or pos[1] < 0:
        return False

    if dest[0] >= gm.size or dest[1] >= gm.size:
        return False
    if dest[0] < 0 or dest[1] < 0:
        return False
    
    if gm.data[dest] is None:
        return False

    gm.data[dest].damage()
    return True

def attackLeft(gm: GameMap, pos: (int, int)):
    dest = (pos[0] - 1, pos[1])

    if pos[0] >= gm.size or pos[1] >= gm.size:
        return False
    if pos[0] < 0 or pos[1] < 0:
        return False

    if dest[0] >= gm.size or dest[1] >= gm.size:
        return False
    if dest[0] < 0 or dest[1] < 0:
        return False
        
    if gm.data[dest] is None:
        return False
        
    gm.data[dest].damage()
    return True

def attackUp(gm: GameMap, pos: (int, int)):
    dest = (pos[0], pos[1] - 1)

    if pos[0] >= gm.size or pos[1] >= gm.size:
        return False
    if pos[0] < 0 or pos[1] < 0:
        return False

    if dest[0] >= gm.size or dest[1] >= gm.size:
        return False
    if dest[0] < 0 or dest[1] < 0:
        return False
        
    if gm.data[dest] is None:
        return False
        
    gm.data[dest].damage()
    return True

actions = {
    MOVE_RIGHT: moveRight,
    MOVE_DOWN: moveDown,
    MOVE_LEFT: moveLeft,
    MOVE_UP: moveUp,
    ATTACK_RIGHT: attackRight,
    ATTACK_DOWN: attackDown,
    ATTACK_LEFT: attackLeft,
    ATTACK_UP: attackUp,
    DO_NOTHING: lambda : True
}

def execute(gm: GameMap, pos: (int, int), action: int):

    if action not in actions:
        raise ("unknown action " + ACTION_NAMES[action])

    return actions[action](gm, pos)

def removeDead(gm: GameMap):
    for pos in gm.data:
        if gm.data[pos] != None and gm.data[pos].health <= 0:
            gm.data[pos] = None

if __name__ == "__main__":

    from GameEntity import *

    print("Move right test")
    gm = GameMap(3)

    gm.data[(1, 1)] = "o"

    gm.printMap()

    execute(gm, (1, 1), MOVE_RIGHT)
    print()

    gm.printMap()
    print("\n")

    print("Move down test")
    gm = GameMap(3)

    gm.data[(1, 1)] = "o"

    gm.printMap()

    execute(gm, (1, 1), MOVE_DOWN)
    print()

    gm.printMap()

    print("\n")

    print("Remove dead test")
    gm = GameMap(3)

    gm.data[(1, 1)] = GameEntity(TYPE_MALE)
    gm.data[(1, 1)].health = 0

    gm.printMap()

    removeDead(gm)
    print()

    gm.printMap()