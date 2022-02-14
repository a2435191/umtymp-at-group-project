from manim import *
import math

class SetupMatrices(Scene):
    def construct(self):
        sigc = MathTex(r'\sigma','=').scale(0.875)
        sigm = Matrix([[1,2,3,4,5], [2,4,3,5,1]]).scale(0.875)
        fullsig = VGroup(sigc, sigm).arrange().shift(UP*1.25)

        gamc = MathTex(r'\gamma','=').scale(0.875)
        gamm = Matrix([[1,2,3,4,5], [5,4,1,2,3]]).scale(0.875)
        fullgam = VGroup(gamc, gamm).arrange().shift(DOWN*1.25)

        self.play(Write(sigc[0]), Write(gamc[0]), Write(sigm.get_brackets()), Write(gamm.get_brackets()), Write(sigc[1]), Write(gamc[1]))
        self.play(Write(sigm.get_entries()), Write(gamm.get_entries()))
        self.wait(0.25)


class Composition1(SetupMatrices):
    def construct(self):
        sigc = MathTex(r'\sigma','=').scale(0.875)
        sigm = Matrix([[1,2,3,4,5], [2,4,3,5,1]]).scale(0.875)
        fullsig = VGroup(sigc, sigm).arrange().shift(UP*1.25)
        gamc = MathTex(r'\gamma','=').scale(0.875)
        gamm = Matrix([[1,2,3,4,5], [5,4,1,2,3]]).scale(0.875)
        fullgam = VGroup(gamc, gamm).arrange().shift(DOWN*1.25)
        t = VGroup(sigc, sigm, fullsig, gamc, gamm, fullgam)
        self.add(t)

        gamsig = MathTex(r'\gamma', r'\sigma', r'=').scale(0.875).shift(5.65026548*LEFT)
        gamsigphantom = MathTex(r'\gamma \sigma =').scale(0.875).shift(5.65026548*LEFT)
        gamsigphantom.set_fill(opacity=0)

        pos1 = [-6.00687928e+00,  0.00000000e+00,  2.13512194e-19]
        pos2 = [-5.74741515e+00,  4.20610313e-02, -5.20437079e-18]
        pos3 = [-5.32416228,  0.05949565,  0.]

        rt = 0.9
        self.play(sigc[0].animate.move_to(pos2), sigc[1].animate.move_to(pos3), gamc[0].animate.move_to(pos1), gamc[1].animate.move_to(pos3), VGroup(gamsigphantom, gamm, sigm).animate.arrange())
        #self.play(ReplacementTransform(VGroup(sigc, gamc), gamsig), VGroup(gamsigphantom, gamm, sigm).animate.arrange())
        self.wait(0.25)
        #print("[0]:", str(gamsig[0].get_center()))
        #print("[1]:", str(gamsig[1].get_center()))
        #print("[2]:", str(gamsig[2].get_center()))
        #self.play(Write(Tex(str(gamsig.get_center()))))
