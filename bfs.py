# Author: Maya Cole
# Date: 11/19/2021
# Purpose: BFS Algorithm

from collections import deque


# Parameters: start vertex, goal vertex
# Purpose: get the path b/wn start and goal
# Return: the path
def BFS(start, goal):
    frontier = deque()
    bkp_d = {}

    frontier.append(start)
    bkp_d[start] = None

    while len(frontier) > 0:
        v = frontier.popleft()
        for x in v.adj_vertices:
            if x not in bkp_d:
                frontier.append(x)
                bkp_d[x] = v

        if goal in bkp_d:
            break

    path = []
    g = goal
    while g != None:
        path.append(g)
        g = bkp_d[g]
    return path
