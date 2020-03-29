import bpy
import house, mail_box, sign, fencepost

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

# init models
house = house.load()
mailbox = mail_box.load()
sign = sign.load()

render(house, (20, 55, 0), "House Left")
render(house, (47.5, 55, 0), "House Right")
render(mailbox, (18.5,56,0), "Mailbox Left")
render(mailbox, (45,56,0), "Mailbox Right")
render(sign, (30,42.5,0), "Sign")

post = fencepost.load()
for i in range(0,8):
    render(post, (20 + (i * 1.25),42.5,0), "Post " + str(i))