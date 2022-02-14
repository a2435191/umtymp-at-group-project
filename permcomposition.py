from manim import *
import math
import numpy as np

class SetupMatrices(Scene):
    def construct(self):
        sf = 1.5
        sigc = MathTex(r'\sigma','=').scale(sf)
        sigm = Matrix([[1,2,3,4,5], [2,4,3,5,1]]).scale(sf)
        fullsig = VGroup(sigc, sigm).arrange().shift(UP*1.75)

        gamc = MathTex(r'\gamma','=').scale(sf)
        gamm = Matrix([[1,2,3,4,5], [5,4,1,2,3]]).scale(sf)
        fullgam = VGroup(gamc, gamm).arrange().shift(DOWN*1.75)

        self.play(Write(sigc[0]), Write(gamc[0]), Write(sigm.get_brackets()), Write(gamm.get_brackets()), Write(sigc[1]), Write(gamc[1]))
        self.play(Write(sigm.get_entries()), Write(gamm.get_entries()))
        self.wait(0.25)


class Composition1(Scene):
    def construct(self):
        sf = 1.5
        sigc = MathTex(r'\sigma','=').scale(sf)
        sigm = Matrix([[1,2,3,4,5], [2,4,3,5,1]]).scale(sf)
        fullsig = VGroup(sigc, sigm).arrange().shift(UP*1.75)
        gamc = MathTex(r'\gamma','=').scale(sf)
        gamm = Matrix([[1,2,3,4,5], [5,4,1,2,3]]).scale(sf)
        fullgam = VGroup(gamc, gamm).arrange().shift(DOWN*1.75)
        t = VGroup(sigc, sigm, fullsig, gamc, gamm, fullgam)
        self.add(t)

        gamsig = MathTex(r'\gamma', r'\sigma', r'=').scale(0.875).shift(5.65026548*LEFT)
        gamsigphantom = MathTex(r'\gamma \sigma =').scale(0.875).shift(5.65026548*LEFT)
        gamsigphantom.set_fill(opacity=0)

        pos1 = [-6.00687928e+00,  0.00000000e+00,  2.13512194e-19]
        pos2 = [-5.74741515e+00,  4.20610313e-02, -5.20437079e-18]
        pos3 = [-5.32416228,  0.05949565,  0.]

        rt = 0.9
        self.play(fullsig.animate.scale(0.875/1.5), fullgam.animate.scale(0.875/1.5))
        self.play(sigc[0].animate.move_to(pos2), sigc[1].animate.move_to(pos3), gamc[0].animate.move_to(pos1), gamc[1].animate.move_to(pos3), VGroup(gamsigphantom, gamm, sigm).animate.arrange())
        #self.play(ReplacementTransform(VGroup(sigc, gamc), gamsig), VGroup(gamsigphantom, gamm, sigm).animate.arrange())
        self.wait(0.25)
        #print("[0]:", str(gamsig[0].get_center()))
        #print("[1]:", str(gamsig[1].get_center()))
        #print("[2]:", str(gamsig[2].get_center()))
        #self.play(Write(Tex(str(gamsig.get_center()))))

class Composition2(Scene):
    def construct(self):
        sigm = Matrix([[1,2,3,4,5], [2,4,3,5,1]]).scale(0.875)
        gamm = Matrix([[1,2,3,4,5], [5,4,1,2,3]]).scale(0.875)
        gamsig = MathTex(r'\gamma', r'\sigma', r'=').scale(0.875).shift(5.65026548*LEFT)
        t = VGroup(gamsig, gamm, sigm).arrange()
        self.add(t)

        sigc = MathTex(r'\sigma','=').scale(1.5)
        gamc = MathTex(r'\gamma','=').scale(1.5)

        self.play(Unwrite(gamsig), sigm.animate.move_to([1.25, 1.75, 0]), gamm.animate.move_to([1.25, -1.75, 0]))
        self.play(sigm.animate.scale(1.5/0.875), gamm.animate.scale(1.5/0.875))
        #self.play(VGroup(sigc, sigm).animate.arrange(), VGroup(gamc, gamm).animate.arrange())

class Composition3(Scene):
    def construct(self):
        sigm = Matrix([[1,2,3,4,5], [2,4,3,5,1]]).scale(1.5)
        gamm = Matrix([[1,2,3,4,5], [5,4,1,2,3]]).scale(1.5)
        sigm.shift(1.75*UP+RIGHT*1.25)
        gamm.shift(1.75*DOWN+RIGHT*1.25)
        self.add(sigm, gamm)

        c1 = MathTex(r'( \gamma','\sigma )(1)=4')
        c2 = MathTex(r'( \gamma \sigma )(2)=2')
        c3 = MathTex(r'( \gamma \sigma )(3)=1')
        c4 = MathTex(r'( \gamma \sigma )(4)=3')
        c5 = MathTex(r'( \gamma \sigma )(5)=5')
        values = VGroup(c1, c2, c3, c4, c5).arrange(DOWN, buff=0.75).shift(LEFT*5.5)

        div = Line(start=[0,5,0], end=[0,-5,0], color=YELLOW)
        div.next_to(c3, RIGHT)
        div.shift(RIGHT*0.25)

        doots = VGroup()
        for i in range(0,15):
            doots.add(Dot(fill_opacity=0))
        doots.arrange_in_grid(buff=(1.8,0.6), rows=3).move_to(VGroup(sigm,gamm).get_center())

        adj = 0.5
        #l1 = DashedLine(start=sigm.get_rows()[1][0].get_center()+DOWN*adj, end=gamm.get_rows()[0][1].get_center()+UP*adj)
        #dl = 0.1
        lpos1 = sigm.get_rows()[1][0].get_center()+DOWN*adj
        lpos2 = sigm.get_rows()[1][0].get_center()+DOWN*1.15

        l1p1 = Line(start=doots[0].get_center(), end=doots[5].get_center())
        l1p2 = l1p1.add_line_to(doots[6].get_center())
        l1p3 = l1p2.add_line_to(doots[11].get_center())
        actualtip = Polygon([-0.075, 0, 0], [0.075, 0,0], [0,-0.15,0], color=WHITE, fill_opacity=1)
        actualtip.move_to(doots[11].get_center()+UP*0.05)
        l1p4 = Line(start=doots[0].get_center(), end=doots[10].get_center())
        actualtip2 = Polygon([-0.075, 0, 0], [0.075, 0,0], [0,-0.15,0], color=WHITE, fill_opacity=1)
        actualtip2.move_to(doots[10].get_center()+UP*0.05)

        l2p1 = Line(start=doots[1].get_center(), end=doots[6].get_center())
        l2p2 = l2p1.add_line_to(doots[8].get_center())
        l2p3 = l2p2.add_line_to(doots[13].get_center())
        at21 = Polygon([-0.075, 0, 0], [0.075, 0,0], [0,-0.15,0], color=WHITE, fill_opacity=1)
        at21.move_to(doots[13].get_center()+UP*0.05)
        l2p4 = Line(start=doots[1].get_center(), end=doots[11].get_center())
        at22 = Polygon([-0.075, 0, 0], [0.075, 0,0], [0,-0.15,0], color=WHITE, fill_opacity=1)
        at22.move_to(doots[11].get_center()+UP*0.05)

        poopymiddle = Line(start=doots[2].get_center(), end=doots[12].get_center())
        pmtip = Polygon([-0.075, 0, 0], [0.075, 0,0], [0,-0.15,0], color=WHITE, fill_opacity=1)
        pmtip.move_to(doots[12].get_center()+UP*0.05)

        l3p1 = Line(start=doots[3].get_center(), end=doots[8].get_center())
        l3p2 = l3p1.add_line_to(doots[9].get_center())
        l3p3 = l3p2.add_line_to(doots[14].get_center())
        at31 = Polygon([-0.075, 0, 0], [0.075, 0,0], [0,-0.15,0], color=WHITE, fill_opacity=1)
        at31.move_to(doots[14].get_center()+UP*0.05)
        l3p4 = Line(start=doots[3].get_center(), end=doots[13].get_center())
        at32 = Polygon([-0.075, 0, 0], [0.075, 0,0], [0,-0.15,0], color=WHITE, fill_opacity=1)
        at32.move_to(doots[13].get_center()+UP*0.05)

        fl = Line(start=doots[4].get_center(), end=doots[14].get_center())
        flt = Polygon([-0.075, 0, 0], [0.075, 0,0], [0,-0.15,0], color=WHITE, fill_opacity=1)
        flt.move_to(doots[14].get_center()+UP*0.05)

        def shiftywifty(a,b):
            return gamm.get_columns()[a].animate.move_to(gamm.get_columns()[b].get_center()), gamm.get_columns()[b].animate.move_to(gamm.get_columns()[a].get_center())

        self.play(Create(doots))

        # p1
        self.play(Create(l1p1), Create(actualtip, lag_ratio=0.75))

        self.wait(0.25)

        self.play(Write(values[0]), Create(div))

        self.play(ReplacementTransform(VGroup(actualtip, l1p1), VGroup(actualtip2, l1p4)), gamm.get_columns()[0].animate.move_to(gamm.get_columns()[1].get_center()), gamm.get_columns()[1].animate.move_to(gamm.get_columns()[0].get_center()))

        self.wait(0.25)

        # p2
        self.play(Uncreate(VGroup(actualtip2, l1p4)), Create(l2p1), Create(at21, lag_ratio=0.75))

        self.wait(0.25)

        self.play(*shiftywifty(0,3), ReplacementTransform(VGroup(l2p1, at21), VGroup(l2p4, at22)))

        self.play(Write(values[1]))

        self.wait(0.25)

        # p3
        self.play(Uncreate(VGroup(at22, l2p4)), Create(poopymiddle), Create(pmtip, lag_ratio=0.75))

        self.play(Write(values[2]))

        self.wait(0.25)

        # p4
        self.play(Uncreate(poopymiddle), Uncreate(pmtip), Create(l3p1), Create(at31, lag_ratio=0.75))

        self.wait(0.25)

        self.play(*shiftywifty(0,4), ReplacementTransform(VGroup(l3p1, at31), VGroup(l3p4, at32)), Write(fl), Write(flt, lag_ratio=0.75))

        self.play(Write(values[3]), Write(values[4]))

        #self.play()
