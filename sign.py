class Sign():
    vertices = [(0,0,0.625),
         (2.5,0,0.625),
         (2.5,0.75,0.625),
         (0,0.75,0.625),
         (0,0,3.125),
         (2.5,0,3.125),
         (2.5,0.75,3.125),
         (0,0.75,3.125),#7
         #Sign part2
         (0.75,0.1875,0),
         (1.6875,0.1875,0),
         (0.75,0.1875,0.625),
         (1.6875,0.1875,0.625),
         (0.75,0.5625,0),
         (1.6875,0.5625,0),
         (0.75,0.5625,0.625),
         (1.6875,0.5625,0.625),#15
         #Sign part3
         (0.75,0.1875,3.125),
         (1.6875,0.1875,3.125),
         (1.6875,0.5625,3.125),
         (0.75,0.5625,3.125),
         (0.75,0.1875,3.25),
         (1.6875,0.1875,3.25),
         (1.6875,0.5625,3.25),
         (0.75,0.5625,3.25)
         ]

    faces = [(0,1,2,3),
            (7,6,5,4),
            (0,4,5,1),
            (1,5,6,2),
            (2,6,7,3),
            (3,7,4,0),
            (8,9,11,10),
            (8,9,13,12),
            (12,13,15,14),
            (8,12,14,10),
            (9,13,15,11),
            (10,14,15,11),
            (16,17,18,19),
            (16,20,23,19),
            (16,20,21,17),
            (17,18,22,21),
            (18,19,23,22),
            (20,21,22,23)
            ]

def load():
    return Sign()
