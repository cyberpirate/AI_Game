
from GameMap import GameMap

MOVE_RIGHT = 0
MOVE_DOWN = 1
MOVE_LEFT = 2
MOVE_UP = 3

ATTAK_RIGHT = 4
ATTAK_DOWN = 5
ATTAK_LEFT = 6
ATTAK_UP = 7

def moveRight(ge: GameMap, pos):

    dest = (pos[0] + 1, pos[1])

    if pos[0] >= ge.size or pos[1] >= ge.size:
        return False
    if pos[0] < 0 or pos[1] < 0:
        return False

    if dest[0] >= ge.size or dest[1] >= ge.size:
        return False
    if dest[0] < 0 or dest[1] < 0:
        return False

    if ge.data[dest] is not None:
        return False
    
    ge.data[dest] = ge.data[pos]
    ge.data[pos] = None
    return True

def moveDown(ge: GameMap, pos):
    dest = (pos[0], pos[1] + 1)

    if pos[0] >= ge.size or pos[1] >= ge.size:
        return False
    if pos[0] < 0 or pos[1] < 0:
        return False

    if dest[0] >= ge.size or dest[1] >= ge.size:
        return False
    if dest[0] < 0 or dest[1] < 0:
        return False
    
    if ge.data[dest] is not None:
        return False

    ge.data[dest] = ge.data[pos]
    ge.data[pos] = None
    return True

def moveLeft(ge: GameMap, pos):
    dest = (pos[0] - 1, pos[1])

    if pos[0] >= ge.size or pos[1] >= ge.size:
        return False
    if pos[0] < 0 or pos[1] < 0:
        return False

    if dest[0] >= ge.size or dest[1] >= ge.size:
        return False
    if dest[0] < 0 or dest[1] < 0:
        return False
        
    if ge.data[dest] is not None:
        return False
        
    ge.data[dest] = ge.data[pos]
    ge.data[pos] = None
    return True

def moveUp(ge: GameMap, pos):
    dest = (pos[0], pos[1] - 1)

    if pos[0] >= ge.size or pos[1] >= ge.size:
        return False
    if pos[0] < 0 or pos[1] < 0:
        return False

    if dest[0] >= ge.size or dest[1] >= ge.size:
        return False
    if dest[0] < 0 or dest[1] < 0:
        return False
        
    if ge.data[dest] is not None:
        return False
        
    ge.data[dest] = ge.data[pos]
    ge.data[pos] = None
    return True

def attackRight(ge: GameMap, pos):

    dest = (pos[0] + 1, pos[1])

    if pos[0] >= ge.size or pos[1] >= ge.size:
        return False
    if pos[0] < 0 or pos[1] < 0:
        return False

    if dest[0] >= ge.size or dest[1] >= ge.size:
        return False
    if dest[0] < 0 or dest[1] < 0:
        return False

    if ge.data[dest] is None:
        return False
    
    ge.data[dest].damage()
    return True

def attackDown(ge: GameMap, pos):
    dest = (pos[0], pos[1] + 1)

    if pos[0] >= ge.size or pos[1] >= ge.size:
        return False
    if pos[0] < 0 or pos[1] < 0:
        return False

    if dest[0] >= ge.size or dest[1] >= ge.size:
        return False
    if dest[0] < 0 or dest[1] < 0:
        return False
    
    if ge.data[dest] is None:
        return False

    ge.data[dest].damage()
    return True

def attackLeft(ge: GameMap, pos):
    dest = (pos[0] - 1, pos[1])

    if pos[0] >= ge.size or pos[1] >= ge.size:
        return False
    if pos[0] < 0 or pos[1] < 0:
        return False

    if dest[0] >= ge.size or dest[1] >= ge.size:
        return False
    if dest[0] < 0 or dest[1] < 0:
        return False
        
    if ge.data[dest] is None:
        return False
        
    ge.data[dest].damage()
    return True

def attackUp(ge: GameMap, pos):
    dest = (pos[0], pos[1] - 1)

    if pos[0] >= ge.size or pos[1] >= ge.size:
        return False
    if pos[0] < 0 or pos[1] < 0:
        return False

    if dest[0] >= ge.size or dest[1] >= ge.size:
        return False
    if dest[0] < 0 or dest[1] < 0:
        return False
        
    if ge.data[dest] is None:
        return False
        
    ge.data[dest].damage()
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

def execute(ge: GameMap, pos, action: int):

    if action not in actions:
        raise ("unknown action " + str(action))

    return actions[action](ge, pos)



if __name__ == "__main__":

    print("Move right test")
    ge = GameMap(3)

    ge.data[(1, 1)] = "o"

    ge.printMap()

    execute(ge, (1, 1), MOVE_RIGHT)
    print()

    ge.printMap()
    print("\n")

    print("Move down test")
    ge = GameMap(3)

    ge.data[(1, 1)] = "o"

    ge.printMap()

    execute(ge, (1, 1), MOVE_DOWN)
    print()

    ge.printMap()