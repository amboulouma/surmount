from math import cos, sin, pi
import numpy as np

def update_coordinate(vertice, x_min, x_max, y_min, y_max, z_min, z_max):
    if x_min > float(vertice[0]):
        x_min = float(vertice[0])
    if x_max < float(vertice[0]):
        x_max = float(vertice[0])
    if y_min > float(vertice[1]):
        y_min = float(vertice[1])
    if y_max < float(vertice[1]):
        y_max = float(vertice[1])
    if z_min > float(vertice[2]):
        z_min = float(vertice[2])
    if z_max < float(vertice[2]):
        z_max = float(vertice[2])
    return x_min, x_max, y_min, y_max, z_min, z_max

def create_vertices(x_min, x_max, y_min, y_max, z_min, z_max):
    # Applying dimensions (Optional when  the max coordinates fits)
    x_max = x_min + 75
    y_max = y_min + 10
    z_max = z_min + 135

    # Creating vertices
    vertices = np.array([[x_min, y_min, z_min],
            [x_max, y_min, z_min],
            [x_max, y_min, z_max],
            [x_min, y_min, z_max],
            [x_min, y_max, z_min],
            [x_max, y_max, z_min],
            [x_max, y_max, z_max],
            [x_min, y_max, z_max]])

    return vertices

def print_files(files):
    for _file in files:
        for line in _file:
            print(line)
        

def output_vertices(_file, vertices):
    for v in vertices:
        _file.write("v {} {} {}\n".format(*v))

def output_standard_faces(files):
    for _file in files:
        _file.write("\nf {} {} {} {}\n".format(1,2,3,4))
        _file.write("f {} {} {} {}\n".format(5,6,7,8))
        _file.write("f {} {} {} {}\n".format(1,5,8,4))
        _file.write("f {} {} {} {}\n".format(2,6,7,3))
        _file.write("f {} {} {} {}\n".format(1,5,6,2))
        _file.write("f {} {} {} {}\n".format(4,8,7,3))

def output_details(files):
    for _file in files:
        _file.write("\n# 8 vertices")
        _file.write("\n# 0 texture params")
        _file.write("\n# 0 normals")
        _file.write("\n# 6 faces")

def translateX(vertices, x):
    for v in vertices:
        v[0] += x

def translateY(vertices, y):
    for v in vertices:
        v[1] += y

def translateZ(vertices, z):
    for v in vertices:
        v[1] += z

def rotateX3D(vertices, theta): 
    for i in range(len(vertices)):
        y = vertices[i][1]
        z = vertices[i][2]
        vertices[i][1] = y * cos(theta*pi/180) - z * sin(theta*pi/180)
        vertices[i][2] = z * cos(theta*pi/180) + y * sin(theta*pi/180)

def rotateY3D(vertices, theta): 
    for i in range(len(vertices)):
        x = vertices[i][0]
        z = vertices[i][2]
        vertices[i][0] = x * cos(theta*pi/180) - z * sin(theta*pi/180)
        vertices[i][2] = z * cos(theta*pi/180) + x * sin(theta*pi/180)
    
def rotateZ3D(vertices, theta): 
    for i in range(len(vertices)):
        x = vertices[i][0]
        y = vertices[i][1]
        vertices[i][0] = x * cos(theta*pi/180) - y * sin(theta*pi/180)
        vertices[i][1] = y * cos(theta*pi/180) + x * sin(theta*pi/180)

def close_files(files):
    for _file in files:
        _file.close()