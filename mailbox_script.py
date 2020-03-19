import bpy

verts = [(0,0,0),
        (0,0.55,0),
        (0.55,0.55,0),
        (0.55,0,0),
        (0,0,1.75),
        (0,0.55,1.75),
        (0.55,0.55,1.75),
        (0.55,0,1.75),
        #start of box
        #box base
        (-0.25,-0.5,1.75),#8
        (-0.25,1.05,1.75),
        (0.8,1.05,1.75),
        (0.8,-0.5,1.75),
        #box body
        (-0.25,-0.5,2.75),#12
        (-0.25,1.05,2.75),
        (0.8,1.05,2.75),
        (0.8,-0.5,2.75)]
        
faces = [(0,1,2,3),
        (0,4,5,1),
        (1,5,6,2),
        (2,6,7,3),
        (3,7,4,0),
        #box faces
        (8,9,10,11),
        (8,9,13,12),
        (9,10,14,13),
        (10,11,15,14),
        (8,11,15,12),
        (12,13,14,15)]

myMesh = bpy.data.meshes.new("Mailbox")
myObj = bpy.data.objects.new("Mailbox", myMesh)

myObj.location = (18.5,56,0)
bpy.context.scene.objects.link(myObj)

myMesh.from_pydata(verts,[],faces)
myMesh.update(calc_edges=True)