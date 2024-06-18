# Author: Maya Cole
# Date: 11/14/ 2021
# Purpose: read the dartmouth graph text file and change the formatting of each line
from Vertex import Vertex


def load_graph(file_name):
    vertex_dict = {}
    file = open(file_name, "r")
    for l in file:
        section_split = l.split(";")
        vertex_name = section_split[0].strip()
        # adjacent_vertices = section_split[1].strip()
        x_y = section_split[2].split(",")
        x = x_y[0].strip()
        y = x_y[1].strip()
        vertex_dict[vertex_name] = Vertex(vertex_name, x, y)

    file.close()
    file = open(file_name, "r")

    for l in file:
        section_split = l.split(";")
        vertex_name = section_split[0]
        adjacent_vertices = section_split[1].split(",")

        for a in adjacent_vertices:
            vertex_dict[vertex_name].adj_vertices.append(vertex_dict[a.strip()])

    file.close()
    return vertex_dict

