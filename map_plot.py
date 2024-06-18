# Author: Maya Cole
# Date: 11/19/2021
# Purpose: display the graph & select the start & goal
from bfs import BFS
from load_graph import load_graph
from cs1lib import *

WIDTH = 1012
HEIGHT = 811

mpressed = False
x1 = 0
y1 = 0
x2 = 0
y2 = 0
start_vertex = None
goal_vertex = None


# Purpose: when the user presses on the keypad/mouse/
# draw pixels & set the current x,y coordinates to/
# the old x,y coordinates
# Parameters: mx the x-coordinate the mouse hovers over/
# my the y-coordinate the mouse hovers over
def my_mpress(mx, my):
    global mpressed, y1, x1
    mpressed = True
    x1 = mx
    y1 = my


# Purpose: when the mouse is released, stop drawing
# Parameters: mx the x-coordinate the mouse hovers over/
# my the y-coordinate the mouse hovers over
def my_mrelease(mx, my):
    global x2, y2, mpressed
    x2 = mx
    y2 = my
    mpressed = False


# Purpose: when the mouse is moved around set the/
# current value to where the mouse is hovering over
# Parameters: mx the x-coordinate the mouse hovers over/
# my the y-coordinate the mouse hovers over
def my_mmove(mx, my):
    global x2, y2
    x2 = mx
    y2 = my


vertex_dict = load_graph("dartmouth_graph.txt")
img = load_image("dartmouth_map.png")


def main_draw():
    global start_vertex, goal_vertex
    draw_image(img, 0, 0)

    for key in vertex_dict:
        v_obj = vertex_dict[key]
        v_obj.vertex_draw(1, 0, 1)
        vertex_dict[key].draw_adj_list(0.8, 0.5, 0.3)

    # get the start vertex
    for key in vertex_dict:
        v_obj = vertex_dict[key]
        if v_obj.smallest(x1, y1):
            start_vertex = v_obj
            start_vertex.vertex_draw(0.8, 0.7, 0.9)

    # get the goal vertex
    if start_vertex != None:
        for key in vertex_dict:
            v_obj = vertex_dict[key]
            if v_obj.smallest(x2, y2):
                goal_vertex = v_obj
                goal_vertex.vertex_draw(0, 0.7, 0.4)

    if start_vertex != None and goal_vertex != None and start_vertex != goal_vertex:
        path = BFS(start_vertex, goal_vertex)

        for x in range(len(path) - 1):
            path[x].vertex_draw(0, 0.3, 0)
            path[x].draw_edge(path[x + 1], 0, 0.3, 0)


start_graphics(main_draw, width=WIDTH, height=HEIGHT, mouse_press=my_mpress, mouse_release=my_mrelease,
               mouse_move=my_mmove)
