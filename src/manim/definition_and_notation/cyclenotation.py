# Written by Pramod Anandarao

from manim import *
import numpy as np
import math

class PermArray(Scene):
    def construct(self):
        arr = MathTex(r'\begin{bmatrix}1&2&3&4&5&6\\2&1&4&6&5&3\end{bmatrix}')
        self.play(Write(arr))

class TextBookCycle1(Scene):
    def construct(self):
        # arcs
        gap = PI/6
        rad = 1.25
        tl = 0.25
        adj = math.acos((2*rad**2-tl**2) / (2*rad**2))

        a2 = Arc(angle=-PI+gap+adj, start_angle=3*PI/2-(gap+adj)/2, radius=rad, arc_center=np.array([0., 0., 0.]))
        a1 = Arc(angle=-PI+gap+adj, start_angle=PI/2-(gap+adj)/2, radius=rad, arc_center=np.array([0., 0., 0.]))

        # tips
        a1.add_tip(tip_length=tl)
        a2.add_tip(tip_length=tl)

        a1.move_arc_center_to(np.array([0., 0., 0.]))
        a2.move_arc_center_to(np.array([0., 0., 0.]))

        # captions
        a1c = MathTex(r'\alpha')
        a1c.next_to(a1, RIGHT)
        a2c = MathTex(r'\alpha')
        a2c.next_to(a2, LEFT)

        # numbers
        adj2 = 0.075
        ap1 = MathTex(r'1').shift(UP*(rad-adj2))
        ap2 = MathTex(r'2').shift(DOWN*(rad-adj2))

        # animations
        self.play(Write(ap1), Create(a1), Write(a1c), Write(ap2))
        self.play(Create(a2), Write(a2c))

class TextBookCycle2(Scene):
    def construct(self):
        # arcs
        gap = PI/6
        a1 = Arc(angle=-2*PI/3+gap, start_angle=PI/2-gap/2, radius=2)
        a2 = Arc(angle=-2*PI/3+gap, start_angle=-PI/6-gap/2, radius=2)
        a3 = Arc(angle=-2*PI/3+gap, start_angle=-5*PI/6-gap/2, radius=2)

        # tips
        a1.add_tip()
        a2.add_tip()
        a3.add_tip()

        # captions
        a2c = MathTex(r'\alpha')
        a2c.next_to(a2, DOWN)
        d = abs(a2c.get_y())
        a1c = MathTex(r'\alpha').shift(d/2*UP + (d/2)*math.sqrt(3)*RIGHT)
        a3c = MathTex(r'\alpha').shift(d/2*UP + (d/2)*math.sqrt(3)*LEFT)

        # numbers
        p1 = MathTex(r'3').shift(UP*2)
        p2 = MathTex(r'4').shift(math.sqrt(3)*RIGHT + DOWN)
        p3 = MathTex(r'6').shift(math.sqrt(3)*LEFT + DOWN)

        # animations
        self.play(Write(p1))
        self.play(Create(a1), Write(a1c))
        self.play(Write(p2))
        self.play(Create(a2), Write(a2c))
        self.play(Write(p3))
        self.play(Create(a3), Write(a3c))

class TextBookCycle3(Scene):
    def construct(self):
        # arcs
        rad = 1.25
        gap = PI/6
        c1 = Arc(angle=-2*PI+gap, start_angle=PI/2-gap/2, radius=rad)
        c1.move_arc_center_to(0)

        # tips
        c1.add_tip()

        # captions
        c1c = MathTex(r'\alpha')
        c1c.next_to(c1, DOWN)

        # numbers
        cp1 = MathTex(r'5').shift(UP*1.25)

        # animations
        self.play(Write(c1), Create(cp1), Create(c1c))

class FullCycle(Scene):
    def construct(self):
        # matrix
        arreq = MathTex(r'\alpha','=')
        arr = Matrix([[1,2,3,4,5,6], [2,1,4,6,5,3]]) #, bracket_h_buff=SMALL_BUFF, bracket_v_buff=SMALL_BUFF)
        fullarr = VGroup(arreq, arr).arrange().shift(UP*2)
        gap = PI/6
        rad = 1.25
        tl = 0.25
        adj = math.acos((2*rad**2-tl**2) / (2*rad**2))

        # surrounding rectangles
        t0 =  SurroundingRectangle(arr.get_columns()[0], color=RED)
        t1 =  SurroundingRectangle(arr.get_columns()[1], color=RED)
        t2 =  SurroundingRectangle(arr.get_columns()[2], color=BLUE)
        t3 =  SurroundingRectangle(arr.get_columns()[3], color=BLUE)
        t4 =  SurroundingRectangle(arr.get_columns()[4], color=GREEN)
        t5 =  SurroundingRectangle(arr.get_columns()[5], color=BLUE)

        # cycles
        # cycle 1
        # arcs
        a2 = Arc(angle=-PI+gap+adj, start_angle=3*PI/2-(gap+adj)/2, radius=rad)
        a1 = Arc(angle=-PI+gap+adj, start_angle=PI/2-(gap+adj)/2, radius=rad)

        # tips
        a1.add_tip(tip_length=tl)
        a2.add_tip(tip_length=tl)

        a1.move_arc_center_to(np.array([0., 0., 0.]))
        a2.move_arc_center_to(np.array([0., 0., 0.]))

        # captions
        a1c = MathTex(r'\alpha')
        a1c.next_to(a1, RIGHT)
        a2c = MathTex(r'\alpha')
        a2c.next_to(a2, LEFT)

        # numbers
        adj2 = rad-0.075
        ap1 = MathTex(r'1', color=RED).shift(UP*adj2)
        ap2 = MathTex(r'2', color=RED).shift(DOWN*adj2)

        fullcycle1 = VGroup(a1, a2, a1c, a2c, ap1, ap2).shift(DOWN*1.5+LEFT*4.5)

        # cycle 2
        # arcs
        adj3=adj
        b1 = Arc(angle=-2*PI/3+gap+adj3, start_angle=PI/2-(gap+adj3)/2, radius=rad+0.1)
        b2 = Arc(angle=-2*PI/3+gap+adj3, start_angle=-PI/6-(gap+adj3)/2, radius=rad+0.1)
        b3 = Arc(angle=-2*PI/3+gap+adj3, start_angle=-5*PI/6-(gap+adj3)/2, radius=rad+0.1)

        # tips
        b1.add_tip(tip_length=tl)
        b2.add_tip(tip_length=tl)
        b3.add_tip(tip_length=tl)

        b1.move_arc_center_to(np.array([0., 0., 0.]))
        b2.move_arc_center_to(np.array([0., 0., 0.]))
        b3.move_arc_center_to(np.array([0., 0., 0.]))

        # captions
        b2c = MathTex(r'\alpha')
        b2c.next_to(b2, DOWN)
        d = abs(b2c.get_y())
        b1c = MathTex(r'\alpha').shift(d/2*UP + (d/2)*math.sqrt(3)*RIGHT)
        b3c = MathTex(r'\alpha').shift(d/2*UP + (d/2)*math.sqrt(3)*LEFT)

        # numbers
        bp1 = MathTex(r'3', color=BLUE).shift(UP*adj2)
        bp2 = MathTex(r'4', color=BLUE).shift((adj2/2)*math.sqrt(3)*RIGHT + DOWN*(adj2/2))
        bp3 = MathTex(r'6', color=BLUE).shift((adj2/2)*math.sqrt(3)*LEFT + DOWN*(adj2/2))

        fullcycle2 = VGroup(b1, b2, b3, b1c, b2c, b3c, bp1, bp2, bp3).shift(DOWN*1.5)

        # cycle 3
        # arcs
        c1 = Arc(angle=-2*PI+PI/4, start_angle=PI/2-(PI/4)/2, radius=0.9375+0.01432466)
        c1.shift(UP*0.375)

        # tips
        c1.add_tip(tip_length=tl)

        # captions
        c1c = MathTex(r'\alpha')
        c1c.next_to(c1, DOWN)

        # numbers
        cp1 = MathTex(r'5', color=GREEN).shift(UP*1.25)

        fullcycle2 = VGroup(c1, c1c, cp1).shift(DOWN*1.5+RIGHT*4.5)

        # animations
        self.play(Write(arreq[0]))
        self.play(Write(arr.get_brackets()), Write(arreq[1]))
        self.play(Write(arr.get_entries()))
        self.wait(0.2)
        self.play(Create(t0), arr.get_columns()[0].animate.set_color(RED))
        self.play(Write(ap1))
        self.play(Create(a1), Write(a1c), Write(ap2))
        self.wait(0.2)
        self.play(ReplacementTransform(t0, t1), arr.get_columns()[1].animate.set_color(RED))
        self.play(Create(a2), Write(a2c))

        self.wait(0.2)
        self.play(ReplacementTransform(t1, t2), arr.get_columns()[2].animate.set_color(BLUE))
        self.play(Write(bp1))
        self.play(Create(b1), Write(b1c), Write(bp2))
        self.wait(0.2)
        self.play(ReplacementTransform(t2, t3), arr.get_columns()[3].animate.set_color(BLUE))
        self.play(Create(b2), Write(b2c), Write(bp3))
        self.wait(0.2)
        self.play(ReplacementTransform(t3, t5), arr.get_columns()[5].animate.set_color(BLUE))
        self.play(Create(b3), Write(b3c))
        self.wait(0.2)

        self.play(Write(cp1), ReplacementTransform(t5, t4), arr.get_columns()[4].animate.set_color(GREEN))
        self.play(Create(c1), Write(c1c))
        self.wait(0.2)
        self.play(Uncreate(t4))
        self.wait(0.2)

        # collapse
        # phantoms
        ccn = MathTex(r'(','1',',','2',')','(','3',',','4',',','6',')','(','5',')').scale(1.5)
        #               0   1   2   3   4   5   6   7   8   9   10  11  12  13  14
        #pc1 = Circle(radius=1.25).shift(DOWN*1.5+LEFT*4.5)
        #pc2 = Circle(radius=1.25).shift(DOWN*1.5)
        #pc3 = Circle(radius=1.25).shift(DOWN*1.5+RIGHT*4.5)

        #self.play(Write(ccn), Create(VGroup(pc1, pc2, pc3)))
        #self.play(MoveAlongPath(bp1, b1))

        #self.play(ReplacementTransform(t0, t1))

        ars = VGroup(a2, a1)
        brs = VGroup(b3, b2, b1)
        crs = VGroup(c1)
        arcremovalsurgery = VGroup(a2, a1, b3, b2, b1, c1)
        labelremovalsurgery = VGroup(a1c, a2c, b1c, b2c, b3c, c1c)

        missingpieces = VGroup(ccn[0], ccn[2], ccn[4], ccn[5], ccn[7], ccn[9], ccn[11], ccn[12], ccn[14])

        #self.play(Write(ccn))

        ccnp1 = ccn[1].get_center()
        ccnp2 = ccn[3].get_center()
        ccnp3 = ccn[6].get_center()
        ccnp4 = ccn[8].get_center()
        ccnp6 = ccn[10].get_center()
        ccnp5 = ccn[13].get_center()

        rt = 2.5

        self.play(Unwrite(labelremovalsurgery, run_time=2.5), Uncreate(arcremovalsurgery, run_time=2.5, lag_ratio=0.1), ap1.animate(run_time=rt).move_to(ccnp1), ap2.animate(run_time=rt).move_to(ccnp2), bp1.animate(run_time=rt).move_to(ccnp3), bp2.animate(run_time=rt).move_to(ccnp4), bp3.animate(run_time=rt).move_to(ccnp6), cp1.animate(run_time=rt).move_to(ccnp5))
        self.play(Write(missingpieces), ap1.animate.scale(1.5), ap2.animate.scale(1.5), bp1.animate.scale(1.5), bp2.animate.scale(1.5), bp3.animate.scale(1.5), cp1.animate.scale(1.5))

        newccn = VGroup(missingpieces, ap1, ap2, bp1, bp2, bp3, cp1)

        self.wait(0.2)

        anl = Tex(r'\underline{Array Notation}').scale(1.5)

        panl = Tex(r'\underline{Array Notation}').scale(1.5)
        panl.set_fill(opacity=0)
        panl.next_to(VGroup(arr, arreq), UP*2)
        cnl = Tex(r'\underline{Cycle Notation}').scale(1.5)

        pcnl = Tex(r'\underline{Cycle Notation}').scale(1.5)
        pcnl.set_fill(opacity=0)
        pcnl.next_to(newccn, UP*2)

        self.play(VGroup(newccn, pcnl).animate.move_to([0,-1.75,0]), VGroup(arr, arreq, panl).animate.move_to([0,1.75,0]))

        anl.next_to(VGroup(arr, arreq), UP*2)
        cnl.next_to(newccn, UP*2)

        #self.play(Write(anl), Write(cnl), Create(SurroundingRectangle(VGroup(arr, anl, arreq)), buff=100), Create(SurroundingRectangle(VGroup(newccn, cnl)), buff=100))

        self.play(Write(anl), Write(cnl))

        self.wait(0.2)
        #self.play(ap1.animate(run_time=rt).move_to(ccnp1), ap2.animate(run_time=rt).move_to(ccnp2), bp1.animate(run_time=rt).move_to(ccnp3), bp2.animate(run_time=rt).move_to(ccnp4), bp3.animate(run_time=rt).move_to(ccnp6), cp1.animate(run_time=rt).move_to(ccnp5))
