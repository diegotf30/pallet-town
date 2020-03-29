class House():
    vertices = [(0, 0, 0), # base level 
        (0, 10, 0), 
        (12.5, 10, 0), 
        (12.5, 0, 0), 
        (0, 0, 3), #second floor
        (0, 10, 3), 
        (12.5, 10, 3), 
        (12.5, 0, 3),
        (6.25, 0, 10), #north-south roof points
        (6.25, 10, 10),
        (0, 2.5, 3), # 10
        (12.5, 2.5, 3), #11
        (12.5, 7.5, 3), #12
        (0, 7.5, 3), #13
        (0, 2.5, 8), # 14
        (12.5, 2.5, 8), #15
        (12.5, 7.5, 8), #16
        (0, 7.5, 8), #17
        (0, 5, 10), #18
        (12.5, 5, 10), #19
        ]
    faces = [(0, 1, 2, 3), # bottom floor 
        (0, 1, 5, 4), # west wall
        (0, 3, 7, 8, 4), # south wall
        (1, 2, 6, 9, 5), # north wall
        (3, 2, 6, 7), # east wall
        (7, 6, 9, 8), # roof east
        (4, 5, 9, 8), #roof west
        (10, 11, 15, 14), #annex south wall
        (13, 12, 16, 17), #annex north wall
        (11, 12, 16, 19, 15), #annex east wall
        (10, 13, 17, 18, 14), #annex west wall
        (14, 15, 19, 18), #annex south roof
        (17, 16, 19, 18), #annex north roof
        ]

def load():
    return House()