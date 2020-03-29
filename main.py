import bpy
import house, mail_box, sign, fencepost, lab, floor, tree

def render(model, location, name):
    if bpy.data.objects.get(name) is not None:
        objs = bpy.data.objects
        objs.remove(objs[name], do_unlink=True)

    #define mesh
    mesh = bpy.data.meshes.new(name)
    object = bpy.data.objects.new(name, mesh)

    #location
    object.location = location
    bpy.context.scene.objects.link(object)

    #create mesh
    mesh.from_pydata(model.vertices, [], model.faces)
    mesh.update(calc_edges=True)
    
def fence(length, loc, count):
    amount = int(length / 1.25)
    for i in range(1, amount):
        render(post, (loc[0] + (i * 1.25),loc[1],loc[2]), "Post " + str(count + i))
    return count + amount

# init models
house = house.load()
mailbox = mail_box.load()
sign = sign.load()
post = fencepost.load()
lab = lab.load()
floor = floor.load()
tree = tree.load()

render(floor, (0,0,0), "Floor")
render(house, (20, 55, 0), "House Left")
render(house, (47.5, 55, 0), "House Right")
render(lab, (45,35,0), "Lab")
render(mailbox, (18.5,56,0), "Mailbox Left")
render(mailbox, (45,56,0), "Mailbox Right")
render(sign, (30,42.5,0), "Sign")

c = fence(10,(20,42.5,0), 0)
c = fence(17.5,(45,22.5,0), c)
fence(20,(35,5,0), c)

def forest(start, end):
    startX = int(start[0] / 3)
    startY = int(end[0] / 4)
    endX = int(start[1] / 3)
    endY = int(end[1] / 4)
    for x in range(startX, endX):
        for y in range(startY, endY):
            render(tree, (1 + x * 4, 1 + y * 4, 0), "Tree " + str(x) + "," + str(y))


for x in range(0, 26):
    for y in range(0, 100):
        name = "Tree " + str(x) + "," + str(y)
        if bpy.data.objects.get(name) is not None:
            objs = bpy.data.objects
            objs.remove(objs[name], do_unlink=True)
# Left side
forest((0, 20),(0, 25))
forest((0, 10),(25, 90))
# Top side
forest((0, 75),(80, 100))
# Right side
forest((50, 75),(0, 25))
forest((65, 75),(25, 90))