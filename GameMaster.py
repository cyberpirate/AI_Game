
import random
from GameHistory import GameHistory
from GameMap import GameMap
from GameEntity import GameEntity
from GameAI import KillAI
from GameConstants import *
import time
import utils

NUM_TYPES = {
    TYPE_MALE: 10,
    # TYPE_FEMALE: 3,
    TYPE_WOLF: 10,
}

class GameMaster:

    def __init__(self, size: int = 10):

        self.size = size

    def initGameMap(self, entityList: [GameEntity] = None):

        gm = GameMap(self.size)

        spotsLeft = [ pos for pos in gm.data if gm.data[pos] == None ]

        random.shuffle(spotsLeft)

        if entityList == None:
            entityList = []
            for t in NUM_TYPES:
                for n in range(NUM_TYPES[t]):
                    entityList.append(GameEntity(t, KillAI()))

        if len(spotsLeft) < len(entityList):
            raise "Not enough spots for entites"

        spotsLeft = spotsLeft[:len(entityList)]

        for x in zip(spotsLeft, entityList):
            gm.data[x[0]] = x[1]

        return gm

    def checkGameEnd(self, gm: GameMap):
        players = [ pos for pos in gm.data if gm.data[pos] != None ]
        wolves = [ pos for pos in players if gm.data[pos].type == TYPE_WOLF ]
        people = [ pos for pos in players if gm.data[pos].type == TYPE_MALE or gm.data[pos].type == TYPE_FEMALE ]
        return len(wolves) == 0 or len(people) == 0

    def runGame(self, gm: GameMap = None, timePerTurn: float = 0):

        if gm is None:
            gm = self.initGameMap()
        gh = GameHistory(gm)

        if timePerTurn > 0:
            utils.clearScreen()
            gm.printMap()
            time.sleep(timePerTurn)

        turn = 0
        while True:

            if self.checkGameEnd(gm):
                break

            playerPos = [ pos for pos in gm.data if gm.data[pos] != None ]
            
            random.shuffle(playerPos)

            for pos in playerPos:

                player = gm.data[pos]

                if player is None:
                    continue

                vision = gm.getVision(pos, 5)
                gh.actions.append((pos, player.ai.getAction(vision)))
                gh.applyAction(gm)
            
            turn += 1

            if timePerTurn > 0:
                utils.clearScreen()
                gm.printMap()
                print("turn: " + str(turn))
                time.sleep(timePerTurn)

        if timePerTurn > 0:
            print("done in %d turns" % turn)

        

if __name__ == "__main__":

    gMaster = GameMaster()
    gMaster.initGameMap().printMap()

    gMaster.runGame(timePerTurn=0.25)