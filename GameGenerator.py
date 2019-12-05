
from GameConstants import *
from GameMaster import GameMaster
from GameEntity import GameEntity
from GameAI import KillAI

def generateBasicData(n: int = 100):

    ret = []
    gm = GameMaster()

    for i in range(n):

        entityList = []

        for x in range(5):
            entityList.append(GameEntity(TYPE_MALE, KillAI()))

        for x in range(5):
            entityList.append(GameEntity(TYPE_WOLF, KillAI()))
        
        gMap = gm.initGameMap(entityList)

        ret.append(gm.runGame(gMap))
    
    return ret


if __name__ == "__main__":

    data = generateBasicData()

    for d in data:
        print(len(d.actions))