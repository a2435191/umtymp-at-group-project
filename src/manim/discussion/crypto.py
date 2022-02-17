from manim import *
from numpy import array
import math
import string

class CaesarCypher(Scene):
    def construct(self):
        pmatrix = Matrix([list(string.ascii_uppercase),list(string.ascii_uppercase)])

        rectt = Rectangle(width=28, height=14/26, grid_xstep=14/26, color=BLUE).shift(UP)
        rectb = Rectangle(width=28, height=14/26, grid_xstep=14/26, color=RED).shift(DOWN)

        linet = Line(start=[-8,0,0], end=[8,0,0], color=BLUE)
        lineb = Line(start=[-8,0,0], end=[8,0,0], color=RED)
        linet.next_to(rectt, UP*14/6.5)
        lineb.next_to(rectb, DOWN*14/6.5)

        capt = Tex('Plain Alphabet').scale(0.75)
        capb = Tex('Cipher Alphabet').scale(0.75)
        capt.shift(UP*(1+14/26))
        capb.shift(DOWN*(1+14/26))

        letterst = VGroup(*[Text(i, font='Courier New') for i in 3*string.ascii_uppercase])
        lettersb = VGroup(*[Text(i, font='Courier New') for i in 3*string.ascii_uppercase])

        numst = VGroup(*[Tex(str(i)).scale(0.75) for i in 3*[j for j in range(26)]])
        numsb = VGroup(*[Tex(str(i)).scale(0.75) for i in 3*[j for j in range(26)]])

        for i in range(78):
            letterst[i].move_to([-14-7+7/26+14/26*i,1,0])
            lettersb[i].move_to([-14-7+7/26+14/26*i,-1,0])
            numst[i].move_to([-14-7+7/26+14/26*i,1,0])
            numsb[i].move_to([-14-7+7/26+14/26*i,-1,0])

        #def arrows(shift):
        #    o = VGroup(*[Arrow(start=[0,0.75,0], end=[shift*14/26,-0.75,0], tip_length=0.2, color=YELLOW, stroke_width=2) for i in range(26)])
        #    for i in range(26):
        #        o[i].move_to([-7+14/26*i+7/26+(shift*10.5/26)/2, 0, 0])
        #    return o

        arr0 = VGroup(*[Arrow(start=[0,0.75,0], end=[0,-0.75,0], tip_length=0.15, color=YELLOW, stroke_width=4) for i in range(26*3)])
        for i in range(26*3):
                arr0[i].move_to([-14-7+14/26*i+7/26, 0, 0])


        arr3 = VGroup(*[Arrow(start=[0,0.75,0], end=[-3*14/26-7/26-7/52,-0.75,0], tip_length=0.15, color=YELLOW, stroke_width=4) for i in range(26*3)])
        for i in range(26*3):
                arr3[i].move_to([-14-7+14/26*(i+2+7/26)-7/52, 0, 0])

        #for i in range(26):
        #    arrows[i].move_to([-7+14/26*i+7/26, 0, 0])

        #self.add(rectt, rectb, letterst, lettersb, linet, lineb, capt, capb)
        self.play(Create(rectt), Create(rectb), Write(letterst), Write(lettersb), Write(linet), Write(lineb), Write(capt), Write(capb))

        self.wait(2)

        self.play(Write(arr3))
        self.play(ReplacementTransform(arr3, arr0), VGroup(lettersb, rectb).animate.shift(RIGHT*3*14/26))


        #self.play(numsb.animate.shift(RIGHT*14/26*3), rectb.animate.shift(RIGHT*14/26*3))

        self.wait(0.2)
