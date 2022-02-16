from manim import *
import numpy as np
from numpy import array
from util_write_group_defs import write_group_defs
import math

class DihedralSet(Scene):
    def construct(self):
        write_group_defs(
            self, "Dihedral Group", "D_4", 
            ["R_0","R_{90}","R_{180}","R_{270}","H","V","D","D'"],
            r"\circ"
        )

class IntroduceSquary(Scene):
    def construct(self):
        #square = Square(side_length=4.0)
        square = Line(start=[2,-2,0], end=[2,2,0])
        square.add_line_to(array([-2,2,0]))
        square.add_line_to(array([-2,-2,0]))
        square.add_line_to(array([2,-2,0]))
        rad = 0.3
        cornerdots = VGroup(Dot(point=[2,-2,0], radius=rad, color=BLUE).set_stroke(width=4).set_fill(color=BLACK), Dot(point=[2,2,0], radius=rad, color=RED).set_stroke(width=4).set_fill(color=BLACK), Dot(point=[-2,2,0], radius=rad, color=GREEN).set_stroke(width=4).set_fill(color=BLACK), Dot(point=[-2,-2,0], radius=rad, color=ORANGE).set_stroke(width=4).set_fill(color=BLACK))

        corn0 = MathTex(r'\alpha').set_stroke(width=1.5).set_fill(opacity=0)
        corn1 = MathTex(r'\beta').set_stroke(width=1.5).set_fill(opacity=0)
        corn2 = MathTex(r'\gamma').set_stroke(width=1.5).set_fill(opacity=0)
        corn3 = MathTex(r'\delta').set_stroke(width=1.5).set_fill(opacity=0)

        corn0.move_to(cornerdots[0].get_center())
        corn1.move_to(cornerdots[1].get_center())
        corn2.move_to(cornerdots[2].get_center())
        corn3.move_to(cornerdots[3].get_center())
        cornerlabels = VGroup(corn0, corn1, corn2, corn3)

        lab0 = MathTex(r'1').next_to(corn0, DOWN+RIGHT)
        lab1 = MathTex(r'2').next_to(corn1, UP+RIGHT)
        lab2 = MathTex(r'3').next_to(corn2, UP+LEFT)
        lab3 = MathTex(r'4').next_to(corn3, DOWN+LEFT)
        staticlabels = VGroup(lab0, lab1, lab2, lab3)

        self.add_foreground_mobjects(corn0, corn1, corn2, corn3)

        r90text = Tex(r'Rotation by $90^\circ$')
        r90eq = MathTex(r'\rho','=')
        r90matrix = Matrix([[1,2,3,4],[2,3,4,1]])
        r90matrix.next_to(r90eq, RIGHT)
        VGroup(r90matrix, r90eq).move_to([0,0,0])
        r90text.next_to(r90matrix, UP)
        r90all = VGroup(r90text, r90eq, r90matrix)
        r90all.move_to([-3,0,0])
        r90textunderline = Line(start=r90matrix.get_brackets()[0].get_center()+UP, end=r90matrix.get_brackets()[1].get_center()+UP).set_stroke(width=2)

        refltext = Tex(r'Horizontal Reflection').move_to(r90text.get_center())
        refleq = MathTex(r'\phi','=')
        reflmatrix = Matrix([[1,2,3,4],[2,1,4,3]])
        reflmatrix.move_to(r90matrix.get_center())
        refleq.next_to(reflmatrix, LEFT)

        self.play(Create(square, run_time=3), Write(cornerdots), Write(cornerlabels), lag_ratio=0.25)
        #self.play()
        #self.play(cornerlabels.animate.set_fill(opacity=1))

        self.wait(0.25)

        self.play(Write(VGroup(lab0, lab1, lab2, lab3)))


        corn0.add_updater(lambda m: corn0.move_to(cornerdots[0].get_center()))
        corn1.add_updater(lambda m: corn1.move_to(cornerdots[1].get_center()))
        corn2.add_updater(lambda m: corn2.move_to(cornerdots[2].get_center()))
        corn3.add_updater(lambda m: corn3.move_to(cornerdots[3].get_center()))

        self.wait(2)

        self.play(VGroup(square, cornerdots, lab0, lab1, lab2, lab3).animate.shift(RIGHT*3.5))

        f=1/2
        arrow12 = CurvedArrow(start_point=corn0.get_center()+RIGHT*f, end_point=corn1.get_center()+RIGHT*f, angle=PI/4, tip_length=0.3, color=YELLOW)
        arrow23 = CurvedArrow(start_point=corn1.get_center()+UP*f, end_point=corn2.get_center()+UP*f, angle=PI/4, tip_length=0.3, color=YELLOW)
        arrow34 = CurvedArrow(start_point=corn2.get_center()+LEFT*f, end_point=corn3.get_center()+LEFT*f, angle=PI/4, tip_length=0.3, color=YELLOW)
        arrow41 = CurvedArrow(start_point=corn3.get_center()+DOWN*f, end_point=corn0.get_center()+DOWN*f, angle=PI/4, tip_length=0.3, color=YELLOW)

        self.play(Write(r90text), Write(r90eq), Write(r90matrix.get_brackets()), Write(r90matrix.get_rows()[0]), Write(r90textunderline))

        self.wait(2)

        rt = 2
        self.play(Rotate(VGroup(square, cornerdots), PI/2, run_time=1), Create(arrow12, run_time=rt), Create(arrow23, run_time=rt), Create(arrow34, run_time=rt), Create(arrow41, run_time=rt)) #90 degree counterclockwise

        self.wait(2)

        self.play(Write(r90matrix.get_rows()[1]))

        self.wait(2)

        self.play(Uncreate(VGroup(arrow41, arrow34, arrow23, arrow12)), Unwrite(r90matrix.get_rows()[1]), Unwrite(r90eq[0]), Unwrite(r90text))

        self.wait(2)

        arrowR = CurvedDoubleArrow(start_point=corn0.get_center()+RIGHT*f, end_point=corn3.get_center()+RIGHT*f, angle=0, tip_length=0.3, color=YELLOW)
        arrowL = CurvedDoubleArrow(start_point=corn2.get_center()+LEFT*f, end_point=corn1.get_center()+LEFT*f, angle=0, tip_length=0.3, color=YELLOW)

        self.play(Write(refleq[0]), Write(refltext))

        self.wait(2)

        #self.play(VGroup(square, cornerdots).animate.flip(axis=array([1,0,0]))) #horizontal reflection
        rt = 0.75
        self.play(Create(arrowR, run_time=1), Create(arrowL, run_time=1), square.animate(run_time=rt).flip(axis=array([1,0,0])), VGroup(corn0, cornerdots[0]).animate(run_time=rt).move_to(cornerdots[3].get_center()), VGroup(corn3, cornerdots[3]).animate(run_time=rt).move_to(cornerdots[0].get_center()), VGroup(corn1, cornerdots[1]).animate(run_time=rt).move_to(cornerdots[2].get_center()), VGroup(corn2, cornerdots[2]).animate(run_time=rt).move_to(cornerdots[1].get_center()))#, corn3.animate.move_to(corn0.get_center()), corn2.animate.move_to(corn3.get_center()), corn3.animate.move_to(corn2.get_center()))

        self.wait(2)

        self.play(Write(reflmatrix.get_rows()[1]))

        self.wait(2)

        self.play(Uncreate(arrowR), Uncreate(arrowL))

        self.wait(0.2)
