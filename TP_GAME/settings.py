from constantes import *

level_map = [
    '     P                        ',
    '     B   Z    C        Z B   X',
    'B    X  B  B  B  B  B  B X  XX',
    'XB   XXXXXXXXXXXXXXXXXXXXX    ',
    'XX                            ',
    '                    Z         ',
    '   B    B  B  B  B B B B      ',
    '   XXX  X  X  X  XXXXXXX      ',
    '                             B',
    '                        Z BXXX',
    '  B  B  B  B  B  B  Z BXXXXXXX',
    'XXXXXXTTXTTXTTXTTXXXXXXXXXXXXX',
]

tile_size = 70

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = len(level_map) * tile_size # 10 * 90 = 900px


# print(len(level_map))
# print(SCREEN_HEIGHT)