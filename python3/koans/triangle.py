#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    list = [a, b, c]
    if a < 1 or b < 1 or c < 1:
        raise(TriangleError)
    elif True in list:
       raise(TriangleError)
    if list.count(1) == 2 or list.count(2) == 2:
       raise(TriangleError)

    if a == b and a == c and b == c:
        return 'equilateral'
    elif list.count(a) == 2 or list.count(c) == 2:
        return 'isosceles'
    else:
        return 'scalene'




# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
