
from GameMap import GameMap
import copy
import GameMove
import time
import utils

class GameHistory:

    def __init__(self, gm:GameMap):

        # initial game state
        self.startingState = copy.deepcopy(gm)

        # game actions stored as [((x, y), action)]
        self.actions = []

    def applyAction(self, gameState:GameMap, i:int = -1):
        if i == -1:
            i = len(self.actions)-1
        GameMove.execute(gameState, self.actions[i][0], self.actions[i][1])
        GameMove.removeDead(gameState)

    def calcState(self, n:int):
        if n > len(self.actions):
            raise "not enough actions"

        gameState = copy.deepcopy(self.startingState)
        
        for i in range(n):
            self.applyAction(gameState, i)
        
        return gameState

    def getAllStates(self):

        ret = []

        gameState = copy.deepcopy(self.startingState)
        ret.append(copy.deepcopy(gameState))

        for i in range(len(self.actions)):
            self.applyAction(gameState, i)
            ret.append(copy.deepcopy(gameState))

        return ret

    def displayGame(self, timePerTurn: float = 0.5):
        i = 1
        for state in self.getAllStates():
            utils.clearScreen()
            state.printMap()
            print("%d / %d" % (i, len(self.actions)+1))
            i += 1
            time.sleep(timePerTurn)

if __name__ == "__main__":

    import GameEntity
    from GameConstants import *

    gm = GameMap(5)

    gm.data[(2, 2)] = GameEntity.GameEntity(TYPE_MALE)

    gh = GameHistory(gm)

    gh.actions.append(((2, 2), GameMove.MOVE_UP))
    gh.actions.append(((2, 1), GameMove.MOVE_UP))

    for state in gh.getAllStates():
        state.printMap()
        print()
    
    for i in range(len(gh.actions)+1):
        gh.calcState(i).printMap()
        print()

    time.sleep(1)

    gh.displayGame()