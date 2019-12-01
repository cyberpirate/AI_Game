
import random
from GameMap import GameMap
from GameConstants import *

class GameAI:

    def __init__(self):
        pass

    def getAction(self, vision: GameMap):
        return random.choice(ACTION_LIST)

class KillAI(GameAI):

    def __init__(self, killFriends:bool =False):
        self.killFriends = killFriends

    def getAction(self, vision: GameMap):
        center = vision.getCenter()

        targets = [ key for key in vision.data if key != center ]
        targets = [ key for key in targets if vision.data[key] != None ]
        targets = [ key for key in targets if vision.data[key].type != TYPE_BARRIER ]
        if not self.killFriends:
            targets = [ key for key in targets if vision.data[key].type != vision.data[center].type ]

        if len(targets) == 0:
            dirs = {
                MOVE_RIGHT: (center[0] + 1, center[1]),
                MOVE_DOWN: (center[0], center[1] + 1),
                MOVE_LEFT: (center[0] - 1, center[1]),
                MOVE_UP: (center[0], center[1] - 1),
            }

            dirs = [ d for d in dirs if vision.data[dirs[d]] is None ]

            if len(dirs) == 0:
                return random.choice(ACTION_LIST)
            
            return random.choice(dirs)
            

        dist = [ abs(center[0] - pos[0]) + abs(center[1] - pos[1]) for pos in targets ]
        
        closestTarget = len(dist)-1
        for i in range(len(dist)-1):
            if dist[i] < dist[closestTarget]:
                closestTarget = i
        
        target = targets[closestTarget]

        if dist[closestTarget] == 1:
            dirs = {
                (center[0] + 1, center[1]): ATTACK_RIGHT,
                (center[0], center[1] + 1): ATTACK_DOWN,
                (center[0] - 1, center[1]): ATTACK_LEFT,
                (center[0], center[1] - 1): ATTACK_UP,
            }
            return dirs[target]
        
        dirs = {
            MOVE_RIGHT: (center[0] + 1, center[1]),
            MOVE_DOWN: (center[0], center[1] + 1),
            MOVE_LEFT: (center[0] - 1, center[1]),
            MOVE_UP: (center[0], center[1] - 1),
        }

        newDirs = {}
        for d in dirs:
            if vision.data[dirs[d]] == None:
                newDirs[d] = dirs[d]
        dirs = newDirs

        if len(dirs) == 0:
            return DO_NOTHING

        ret = random.choice([ d for d in dirs ])
        for d in dirs:
            retDist = abs(center[0] - dirs[ret][0]) + abs(center[1] - dirs[ret][1])
            dirDist = abs(center[0] - dirs[  d][0]) + abs(center[1] - dirs[  d][1])
            if dirDist < retDist:
                ret = d
        
        return ret


if __name__ == "__main__":

    import GameEntity

    print("Test kill ai")

    gm = GameMap(3)

    gm.data[(1, 1)] = GameEntity.GameEntity(TYPE_WOLF)

    ai = KillAI()

    print(ACTION_NAMES[ai.getAction(gm)])
    
    gm.data[(0, 0)] = GameEntity.GameEntity(TYPE_MALE)
    print(ACTION_NAMES[ai.getAction(gm)])

    gm.data[(0, 0)] = None
    gm.data[(0, 1)] = GameEntity.GameEntity(TYPE_MALE)
    print(ACTION_NAMES[ai.getAction(gm)])
