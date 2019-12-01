
from GameMap import GameMap
from GameConstants import *

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

    import GameEntity

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

    gm.data[(1, 1)] = GameEntity.GameEntity(TYPE_MALE)
    gm.data[(1, 1)].health = 0

    gm.printMap()

    removeDead(gm)
    print()

    gm.printMap()