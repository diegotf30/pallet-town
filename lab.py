def face(start):
    faces = [(0,1,2,3),
        (0,4,5,1),
        (1,5,6,2),
        (2,6,7,3),
        (3,7,4,0),
        (4,5,6,7)
        ]
    res = []
    for face in faces:
        res.append(tuple(x + start for x in face))
    return res

def verts(points, heights):
    x1 = points[0]
    x2 = points[1]
    y1 = points[2]
    y2 = points[3]
    low = heights[0]
    top = heights[1]
    return [(x1, y1, low),
        (x1, y2, low),
        (x2, y2, low),
        (x2, y1, low),
        (x1, y1, top),
        (x1, y2, top),
        (x2, y2, top),
        (x2, y1, top),
        ]

class Lab():
    vertices = verts((1.25, 16.25, 1.25, 8.75), (0,4.5)) # Base
    vertices += verts((0, 1.25, 0, 10), (3.5,5.5)) # Left Wall
    vertices += verts((1.25, 17.5, 0, 1.25), (3.5,5.5)) # Front Wall
    vertices += verts((1.25, 17.5, 8.75, 10), (3.5,5.5)) # Back Wall
    vertices += verts((16.25, 17.5, 1.25, 8.75), (3.5,5.5)) # Right Wall
    vertices += [(11,2.25,4.5), # Bottom Part of Chimney
            (11,7.75,4.5),
            (15,7.75,4.5),
            (15,2.25,4.5),
            (12,3.25,6),
            (12,6.75,6),
            (14,6.75,6),
            (14,3.25,6),
        ]
    vertices += verts((12, 14, 3.25, 6.75), (6,9.5)) # Top Part of Chimney

    faces = []
    for i in range(0,56,8):
        faces += face(i)

def load():
    return Lab()