from constantes import *

level_map = [
    '                              ',
    '     B        E          B   X',
    'B    X  B  B  B  B  B  B X  XX',
    'XB   XXXXXXXXXXXXXXXXXXXXX    ',
    'XX                            ',
    '                    N         ',
    '   B    B  B  B  B B B B      ',
    'P  XXX  X  X  X  XXXXXXX      ',
    '                           N B',
    '                          BXXX',
    '  B  B  B  B  B  B    BXXXXXXX',
    'XXXXXXTTXTTXTTXTTXXXXXXXXXXXXX',
]

tile_size = 70

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = len(level_map) * tile_size # 10 * 90 = 900px


# print(len(level_map))
# print(SCREEN_HEIGHT)