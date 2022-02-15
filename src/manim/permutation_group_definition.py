from manim import *
import numpy as np
from numpy import array
from copy import deepcopy
import math


class PermutationGroupDefinition(Scene):
    def construct(self):
        r = 0.5

        michael = Circle(radius=r, color='#0000FF', fill_color='#0000FF', fill_opacity=0.75)
        pramod = Circle(radius=r, color='#FF0000', fill_color='#FF0000', fill_opacity=0.75)
        will = Circle(radius=r, color='#FFFF00', fill_color='#FFFF00', fill_opacity=0.75)
        michael.move_to(array([-2, 0, 0]))
        will.move_to(array([2, 0, 0]))

        arr = [michael, pramod, will]
        ref_arr = deepcopy(arr)
        pos = [array([-2, 0, 0]), array([0, 0, 0]), array([2, 0, 0])]
        right = [Arc(radius=1, start_angle=PI, angle=PI).shift(array([1, 0, 0])),
                 Arc(radius=1, start_angle=0, angle=PI).shift(array([1, 0, 0]))]
        left = [Arc(radius=1, start_angle=PI, angle=-PI).shift(array([-1, 0, 0])),
                 Arc(radius=1, start_angle=0, angle=-PI).shift(array([-1, 0, 0]))]

        self.play(
            *[Create(obj) for obj in arr]
        )

        self.play(
            MoveAlongPath(arr[1], right[0]),
            MoveAlongPath(arr[2], right[1])
        )

        self.play(
            MoveAlongPath(arr[0], left[0]),
            MoveAlongPath(arr[2], left[1])
        )

        self.play(
            MoveAlongPath(arr[0], right[0]),
            MoveAlongPath(arr[1], right[1])
        )

        self.play(
            MoveAlongPath(arr[2], left[0]),
            MoveAlongPath(arr[1], left[1])
        )

        self.play(
            MoveAlongPath(arr[2], right[0]),
            MoveAlongPath(arr[0], right[1])
        )

        self.play(
            MoveAlongPath(arr[1], left[0]),
            MoveAlongPath(arr[0], left[1])
        )



