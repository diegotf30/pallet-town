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

class Floor():
    vertices = verts((0,25,0,100),(0,-3))
    vertices += verts((25,35,25,100),(0,-3))
    vertices += verts((35,100,0,100),(0,-3))
    faces = []
    for i in range(0,24,8):
        faces += face(i)