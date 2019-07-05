#!/usr/bin/env python
# coding=utf-8
def coloring(G):
    color = 0
    groups = set()
    verts =  Verticles(G)
    while verts:
        new_group = set()
        for v in list(verts):
            if not_adjacent_with_set(v, new_group,G):

                new_group.add(V)
                verts.remove(v)
        groups.add((color, new_group))
        color += 1
    return groups
