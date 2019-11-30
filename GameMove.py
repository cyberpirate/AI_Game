
from GameMap import GameMap

MOVE_RIGHT = 0
MOVE_DOWN = 1
MOVE_LEFT = 2
MOVE_UP = 3

ATTAK_RIGHT = 4
ATTAK_DOWN = 5
ATTAK_LEFT = 6
ATTAK_UP = 7

def moveRight(gm: GameMap, pos):

    dest = (pos[0] + 1, pos[1])

    if pos[0] >= gm.size or pos[1] >= gm.size:
        return False
    if pos[0] < 0 or pos[1] < 0:
        return False

    if dest[0] >= gm.size or dest[1] >= gm.size:
        return False
    if dest[0] < 0 or dest[1] < 0:
        return False

    if gm.data[dest] is not None:
        return False
    
    gm.data[dest] = gm.data[pos]
    gm.data[pos] = None
    return True

def moveDown(gm: GameMap, pos):
    dest = (pos[0], pos[1] + 1)

    if pos[0] >= gm.size or pos[1] >= gm.size:
        return False
    if pos[0] < 0 or pos[1] < 0:
        return False

    if dest[0] >= gm.size or dest[1] >= gm.size:
        return False
    if dest[0] < 0 or dest[1] < 0:
        return False
    
    if gm.data[dest] is not None:
        return False

    gm.data[dest] = gm.data[pos]
    gm.data[pos] = None
    return True

def moveLeft(gm: GameMap, pos):
    dest = (pos[0] - 1, pos[1])

    if pos[0] >= gm.size or pos[1] >= gm.size:
        return False
    if pos[0] < 0 or pos[1] < 0:
        return False

    if dest[0] >= gm.size or dest[1] >= gm.size:
        return False
    if dest[0] < 0 or dest[1] < 0:
        return False
        
    if gm.data[dest] is not None:
        return False
        
    gm.data[dest] = gm.data[pos]
    gm.data[pos] = None
    return True

def moveUp(gm: GameMap, pos):
    dest = (pos[0], pos[1] - 1)

    if pos[0] >= gm.size or pos[1] >= gm.size:
        return False
    if pos[0] < 0 or pos[1] < 0:
        return False

    if dest[0] >= gm.size or dest[1] >= gm.size:
        return False
    if dest[0] < 0 or dest[1] < 0:
        return False
        
    if gm.data[dest] is not None:
        return False
        
    gm.data[dest] = gm.data[pos]
    gm.data[pos] = None
    return True

def attackRight(gm: GameMap, pos):

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

def attackDown(gm: GameMap, pos):
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

def attackLeft(gm: GameMap, pos):
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

def attackUp(gm: GameMap, pos):
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
    ATTAK_RIGHT: attackRight,
    ATTAK_DOWN: attackDown,
    ATTAK_LEFT: attackLeft,
    ATTAK_UP: attackUp,
}

def execute(gm: GameMap, pos, action: int):

    if action not in actions:
        raise ("unknown action " + str(action))

    return actions[action](gm, pos)

def removeDead(gm: GameMap):
    for pos in gm.data:
        if gm.data[pos] is not None and gm.data[pos].health <= 0:
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