import os
import sys

import numpy as np

from utils import *

# Input file
f_input = open("data/body_one_side.obj", "r")

# Output files
f_vertices = open("data/vertices.obj", "w")
f_faces = open("data/faces.obj", "w")
f_light_weight = open("data/lightweighted_obj.obj", "w")
f_transformed_light_weight = open("data/transformed_light_weighted_obj.obj", "w")

# Important coordinates for lightweighted obj file

x_min = y_min = z_min = 10**6
x_max = y_max = z_max = -10**6

for line in f_input:
    print(line)
    # Extracting the faces
    if line[0] == "f":
        f_faces.write(line)
    
    # Extracting the faces
    if line[0] == "v" and line[1] != "n":
        vertice = line.split()[1:]
        # Save the vertices into a separate file
        f_vertices.write(line)

        # Update important coordinates on each loop
        x_min, x_max, y_min, y_max, z_min, z_max = update_coordinate(vertice, 
                                                    x_min, x_max, y_min, y_max, z_min, z_max)

# Creating the vertices
vertices = create_vertices(x_min, x_max, y_min, y_max, z_min, z_max)

# Important distances
width = x_max - x_min
length = y_min - y_max
height = z_max - z_min

# Outputting the vertices
output_vertices(f_light_weight, vertices)

# Translating the object
translateY(vertices, 100)
output_vertices(f_transformed_light_weight, vertices)

# Rotating the object 
rotateZ3D(vertices, 45)

# Outputting the faces
output_standard_faces([f_light_weight, f_transformed_light_weight])

# Outputing details
output_details([f_light_weight, f_transformed_light_weight])

# Closing files
close_files([f_vertices,f_input,f_faces,f_light_weight,f_transformed_light_weight])

# Opening files
f_light_weight = open("data/lightweighted_obj.obj", "r")
f_transformed_light_weight = open("data/transformed_light_weighted_obj.obj", "r")


# Print Files
print_files([f_light_weight, f_transformed_light_weight])

# Closing the files
close_files([f_light_weight,f_transformed_light_weight])



    

