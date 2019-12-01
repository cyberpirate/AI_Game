
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