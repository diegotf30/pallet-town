import bpy

verts = [(0,0,0),
        (0,1,0),
        (1,1,0),
        (1,0,0),
        (0,0,1.75),
        (0,1,1.75),
        (1,1,1.75),
        (1,0,1.75),
        #start of tree
        (-1,-1,1.75),#8
        (-1,2,1.75),
        (2,2,1.75),
        (2,-1,1.75),
        #tip of tree
        (0.5,0.5,8)]#12
        
faces = [(0,1,2,3),
        (0,4,5,1),
        (1,5,6,2),
        (2,6,7,3),
        (3,7,4,0),
        #tree faces
        (8,9,10,11),
        (8,9,12),
        (8,11,12),
        (10,11,12),
        (9,10,12)]

myMesh = bpy.data.meshes.new("Tree")
myObj = bpy.data.objects.new("Tree", myMesh)

myObj.location = (0,0,0)
bpy.context.scene.objects.link(myObj)

myMesh.from_pydata(verts,[],faces)
myMesh.update(calc_edges=True)
