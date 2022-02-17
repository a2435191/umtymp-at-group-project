from manim import *
from numpy import array
import math
import string

class CaesarCypher(Scene):
    def construct(self):
        pmatrix = Matrix([list(string.ascii_uppercase),list(string.ascii_uppercase)])

        rectt = Rectangle(width=28, height=14/26, grid_xstep=14/26, color=RED).shift(UP)
        rectb = Rectangle(width=28, height=14/26, grid_xstep=14/26, color=RED).shift(DOWN)

        letterst = VGroup(*[Text(i, font='Courier New') for i in 3*string.ascii_uppercase])
        lettersb = VGroup(*[Text(i, font='Courier New') for i in 3*string.ascii_uppercase])
        for i in range(78):
            letterst[i].move_to([-14-7+7/26+14/26*i,1,0])
            lettersb[i].move_to([-14-7+7/26+14/26*i,-1,0])

        self.add(rectt, rectb, letterst, lettersb)
        self.play(lettersb.animate.shift(LEFT*14/26*3), rectb.animate.shift(LEFT*14/26*3))
        #self.play(Write(letterst), Write(lettersb))

        self.wait(0.2)
