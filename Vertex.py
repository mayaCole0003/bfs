# Author: Maya Cole
# Date: 11/14/ 2021
# Purpose: create Vertex class

from cs1lib import *

# CONSTANTS
V_RADIUS = 10
E_WIDTH = 2


class Vertex:

    def __init__(self, vertex_name, x, y):
        self.vertex_name = vertex_name
        self.x = int(x)
        self.y = int(y)
        self.adj_vertices = []

    # Purpose: draw a vertex
    # Parameters: r, g, and b
    # Return: N/A
    def vertex_draw(self, r, g, b):
        set_fill_color(r, g, b)
        draw_circle(self.x, self.y, V_RADIUS)

    # Purpose: draws an edge between the Vertex that the method is called on (i.e., self)\
    #  and the other vertex, in the color given by r, g, b.
    # Parameters: r, g, and b
    # Return: N/A
    def draw_edge(self, second_vertex, r, g, b):
        set_stroke_width(E_WIDTH)
        set_stroke_color(r, g, b)
        draw_line(self.x, self.y, second_vertex.x, second_vertex.y)

    # Purpose: takes r, g, b, and draws all the edges between the vertex and all the vertices\
    # in its adjacency list, in the color given by r, g, b.
    # Parameters: r, g, and b
    # Return: N/A
    def draw_adj_list(self, r, g, b):
        for s in self.adj_vertices:
            set_fill_color(r, g, b)
            draw_line(self.x, self.y, s.x, s.y)

    # Purpose: takes as parameters x- and y-coordinates & and return
    # a boolean indicating whether this location is within \
    # the smallest surrounding square for this vertex.)
    # Parameters: x- and y- coordinates
    # Return: True/False
    def smallest(self, x, y):
        if (self.x - V_RADIUS) <= x <= (self.x + V_RADIUS) and (self.y - V_RADIUS) <= y <= (self.y + V_RADIUS):
            return True
        return False

    def __str__(self):
        adj_string = self.adj_vertices[0].vertex_name
        for q in self.adj_vertices:
            if q != self.adj_vertices[0]:
                adj_string += "," + q.vertex_name

        return self.vertex_name + "; Location: " + str(self.x) + ", " + str(
            self.y) + "; Adjacent vertices: " + adj_string
