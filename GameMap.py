
from GameConstants import *

class GameMap:

    def __init__(self, size: int):

        from GameEntity import GameEntity

        self.size = size

        self.data:{(int, int): GameEntity} = {}

        for x in range(size):
            for y in range(size):
                self.data[(x, y)] = None

    def printMap(self):
        print("|" + ("--" * (self.size)) + "|")
        for y in range(self.size):
            print("|", end="")
            for x in range(self.size):
                print(("%2s") % self.data[(x, y)] if self.data[(x, y)] != None else "  ", end="")
            print("|")
        print("|" + ("--" * (self.size)) + "|")

    def getVision(self, pos: (int, int), size: int):

        if size % 2 == 0:
            raise "size in getVision must be odd"

        from GameEntity import GameEntity

        edgeSize = size // 2
        gm = GameMap(size)

        for x in range(size):
            for y in range(size):
                srcX = pos[0] - edgeSize + x
                srcY = pos[1] - edgeSize + y
                gm.data[(x, y)] = self.data[(srcX, srcY)] if (srcX, srcY) in self.data else GameEntity(TYPE_BARRIER)


        return gm

    def getCenter(self):
        return (self.size // 2, self.size // 2)

if __name__ == "__main__":

    print("test basic map")
    gm = GameMap(10)

    for x in range(gm.size):
        gm.data[(x, x)] = x

    gm.printMap()
    print("\n\n")

    print("test x axis")
    gm = GameMap(10)

    for x in range(gm.size):
        gm.data[(x, 0)] = x

    gm.printMap()
    print("\n\n")

    print("test vision algo")
    gm = GameMap(10)

    for x in range(gm.size):
        for y in range(gm.size):
            gm.data[(x, y)] = x+y

    gm = gm.getVision((5, 5), 5)
    gm.printMap()
    print("")
    gm = gm.getVision((5, 5), 5)
    gm.printMap()
