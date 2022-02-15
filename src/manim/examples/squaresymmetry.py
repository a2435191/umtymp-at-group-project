from manim import *
import numpy as np
from numpy import array
import math

class DihedralSet(Scene):
    def construct(self):
        dSet = MathTex(r"D_4","=\{","R_0",",","R_{90}",",","R_{180}",",","R_{270}",",","H",",","V",",","D",",","D'","\}", font_size=72)
        #                 0     1     2    3     4      5     6       7     8       9   10  11  12  13  14  15  16   17

        self.play(Write(dSet))

        self.wait(0.2)

class IntroduceSquary(Scene):
    def construct(self):
        square = Square(side_length=4.0)
        rad = 0.3
        cornerdots = VGroup(Dot(point=[2,-2,0], radius=rad, color=BLUE), Dot(point=[2,2,0], radius=rad, color=RED), Dot(point=[-2,2,0], radius=rad, color=GREEN), Dot(point=[-2,-2,0], radius=rad, color=ORANGE))

        corn0 = MathTex('1').set_fill(opacity=0)
        corn1 = MathTex('2').set_fill(opacity=0)
        corn2 = MathTex('3').set_fill(opacity=0)
        corn3 = MathTex('4').set_fill(opacity=0)

        corn0.move_to(cornerdots[0].get_center())
        corn1.move_to(cornerdots[1].get_center())
        corn2.move_to(cornerdots[2].get_center())
        corn3.move_to(cornerdots[3].get_center())
        cornerlabels = VGroup(corn0, corn1, corn2, corn3)

        corn0.add_updater(lambda m: corn0.move_to(cornerdots[0].get_center()))
        corn1.add_updater(lambda m: corn1.move_to(cornerdots[1].get_center()))
        corn2.add_updater(lambda m: corn2.move_to(cornerdots[2].get_center()))
        corn3.add_updater(lambda m: corn3.move_to(cornerdots[3].get_center()))

        self.add_foreground_mobjects(corn0, corn1, corn2, corn3)

        r90text = Tex(r'\underline{Rotation by $90^\circ$}')
        r90eq = MathTex(r'\rho =')
        r90matrix = Matrix([[1,2,3,4],[2,3,4,1]])
        r90matrix.next_to(r90eq, RIGHT)
        VGroup(r90matrix, r90eq).move_to([0,0,0])
        r90text.next_to(VGroup(r90matrix, r90eq), UP)
        r90all = VGroup(r90text, r90eq, r90matrix)
        r90all.move_to([-3,0,0])

        self.play(Create(square), Create(cornerdots))
        self.play(cornerlabels.animate.set_fill(opacity=1))

        self.wait(2)

        self.play(VGroup(square, cornerdots).animate.shift(RIGHT*3.5))

        self.play(Write(r90text), Write(r90eq), Write(r90matrix.get_brackets()), Write(r90matrix.get_rows()[0]))

        self.wait(2)

        self.play(Rotate(VGroup(square, cornerdots), PI/2)) #90 degree counterclockwise

        self.wait(2)

        self.play(Write(r90matrix.get_rows()[1]))


        #self.play(VGroup(square, cornerdots).animate.flip()) #horizontal reflection

        self.wait(0.2)
